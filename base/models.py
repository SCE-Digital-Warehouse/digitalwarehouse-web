from django.db import models
from django.db.models import F
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.urls import reverse
from django.conf import settings
from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail

from config.settings import PROJECT_NAME
from base.utils import upload_to_path


class User(AbstractUser):
    class Roles(models.TextChoices):
        STUDENT = "student", "סטודנט"
        LECTURER = "lecturer", "מרצה"
        __empty__ = "תבחר/י סוג משתמש"

    identity_num = models.CharField(
        max_length=9,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"[0-9]{9}",
                message="תעודת זהות לא תקינה"
            )
        ])
    mobile_num = models.CharField(
        max_length=10, unique=True,
        validators=[
            RegexValidator(
                regex=r"[05][0-9]{8}",
                message="מספר נייד לא חוקי"
            )])
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
        blank=True
    )
    is_first_login = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_mod = models.BooleanField(default=False)

    class Meta:
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.identity_num}"

    def get_absolute_url(self):
        return reverse("user", kwargs={"user_id": self.pk})

    def promote(self):
        """Promotes a user to the moderator."""
        try:
            moderator = self.moderator
        except Moderator.DoesNotExist:
            moderator = None
        if not moderator and not self.is_admin:
            moderator = Moderator.objects.create(user=self)
            self.is_mod = True
            self.save(update_fields=["is_mod"])
        return moderator

    def demote(self):
        """Demotes a moderator to the regular user."""
        try:
            moderator = self.moderator
        except Moderator.DoesNotExist:
            pass
        else:
            moderator.delete()
            self.is_mod = False
            self.save(update_fields=["is_mod"])

    def cancel_first_login(self):
        self.is_first_login = False
        self.save(update_fields=["is_first_login"])


class Moderator(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column="id"
    )
    add_product = models.BooleanField(default=True)
    edit_product = models.BooleanField(default=True)
    delete_product = models.BooleanField(default=True)
    accept_request = models.BooleanField(default=True)
    reject_request = models.BooleanField(default=True)
    finish_borrowing = models.BooleanField(default=True)
    mark_repaired = models.BooleanField(default=True)
    promoted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.user)

    def get_absolute_url(self):
        return self.user.get_absolute_url()


class Category(models.Model):
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children"
    )
    name = models.CharField(max_length=30, unique=True)
    image_url = models.ImageField(upload_to=upload_to_path)
    times_borrowed = models.IntegerField(default=0)
    times_broken = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def increase_times_borrowed(self):
        self.times_borrowed = F("times_borrowed") + 1
        self.save(update_fields=["times_borrowed"])
        if self.parent:
            self.parent.increase_times_borrowed()

    def increase_times_broken(self):
        self.times_broken = F("times_broken") + 1
        self.save(update_fields=["times_broken"])
        if self.parent:
            self.parent.increase_times_broken()

    def reset_counters(self):
        self.times_borrowed = 0
        self.times_broken = 0
        self.save(update_fields=["times_borrowed", "times_broken"])


class Product(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    stock_num = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=20)
    comments = models.TextField(max_length=200, null=True, blank=True)
    times_borrowed = models.IntegerField(default=0)
    times_broken = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    breakage_reported = models.BooleanField(default=False)
    in_repair = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.stock_num} {self.name}"

    def increase_times_borrowed(self):
        self.times_borrowed = F("times_borrowed") + 1
        self.save(update_fields=["times_borrowed"])
        self.category.increase_times_borrowed()

    def increase_times_broken(self):
        self.times_broken = F("times_broken") + 1
        self.save(update_fields=["times_broken"])
        self.category.increase_times_broken()

    def reset_counters(self):
        self.times_borrowed = 0
        self.times_broken = 0
        self.save(update_fields=["times_borrowed", "times_broken"])

    def change_availability(self):
        self.is_available = not self.is_available
        self.save(update_fields=["is_available"])

    def set_breakage_reported(self):
        self.breakage_reported = not self.breakage_reported
        self.save(update_fields=["breakage_reported"])

    def change_condition(self):
        """Changes the condition of a product."""
        self.in_repair = not self.in_repair
        if self.in_repair:
            self.is_available = False
            self.breakage_reported = False
        else:
            self.is_available = True
        self.save(update_fields=["in_repair",
                  "is_available", "breakage_reported"])


class Request(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    product = models.ForeignKey(
        "Product", on_delete=models.PROTECT)
    comments = models.TextField(max_length=200, null=True, blank=True)
    requested_at = models.DateTimeField(
        auto_now_add=True)
    exp_date_to_borrow = models.DateTimeField()
    exp_date_to_return = models.DateTimeField()

    class Meta:
        unique_together = ("user", "product")
        ordering = ["requested_at", "user"]
        # usage: Request.objects.latest() -> the earliest date of requested_at
        get_latest_by = ["requested_at"]

    """ def save(self, *args, **kwargs):
        if self.pk is None:  # determines whether the instance is new
            for field_name in [
                "camera", "rec", "apple", "tripod",
                "light", "cable", "convertor", "projector"
            ]:
                try:
                    product = getattr(self, field_name)
                except AttributeError:
                    pass
                else:
                    product.is_available = False
                    break
        super(Product, self).save(*args, **kwargs) """

    def save(self, *args, **kwargs):
        if self.pk is None:  # determines whether the instance is new
            self.product.change_availability()
        super().save(*args, **kwargs)

    def accept_request(self):
        Borrowing.objects.create(
            user=self.user,
            product=self.product,
            borrowed_at=self.exp_date_to_borrow,
            date_to_return=self.exp_date_to_return,
        )
        self.delete()

    def reject_request(self):
        self.product.change_availability()
        self.delete()


class Borrowing(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(
        "Product", on_delete=models.PROTECT)
    comments = models.TextField(max_length=200, null=True, blank=True)
    borrowed_at = models.DateTimeField(
        auto_now_add=True)
    date_to_return = models.DateTimeField()
    returned_at = models.DateTimeField(blank=True, null=True)
    notified_at = models.DateTimeField(blank=True, null=True)
    extension_requested = models.BooleanField(default=False)
    additional_days = models.PositiveSmallIntegerField(default=0)

    class Meta:
        unique_together = ("user", "product")
        ordering = ["borrowed_at", "user"]
        get_latest_by = ["date_to_return"]

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.product.increase_times_borrowed()
        super().save(*args, **kwargs)

    def notify_user(self):
        """The method notifies a user one per the day."""
        now = timezone.now()
        if now > self.date_to_return and \
                (not self.notified_at or (now - self.notified_at).total_seconds() >= 216000):
            self.notified_at = now
            self.save(update_fields=["notified_at"])
            subject = "איחור בהחזרת המוצר"
            message = f"""
                הודעה זו נשלחה אליך עקב האיחור שלך בהחזרת המוצר ששאלת.
    
                שם המוצר: {self.product.name}
                מק''ט: {self.product.stock_num}
                תאריך השאלה: {timezone.localtime(self.borrowed_at).strftime("%d/%m/%Y %H:%M")}
                תאריך החזרה הנקבע: {timezone.localtime(self.date_to_return).strftime("%d/%m/%Y %H:%M")}
    
                את/ה מתבקש/ת להחזיר את המוצר בדחיפות, אחרת תיקנס/י.
    
                צוות {PROJECT_NAME}
                """
            email_from = settings.EMAIL_HOST_USER
            email_to = [f"{self.user.email}"]
            send_mail(
                subject,
                message,
                email_from,
                email_to,
                fail_silently=False,
            )

    def request_extension(self, additional_days, comments):
        if additional_days > 0:
            self.additional_days = additional_days
            if comments:
                self.comments = comments
            self.extension_requested = True
            self.save(update_fields=[
                "additional_days",
                "comments",
                "extension_requested"
            ])

    def accept_extension(self):
        if self.additional_days > 0:
            self.date_to_return += timedelta(days=self.additional_days)
            self.additional_days = 0
            self.extension_requested = False
            self.comments = None
            self.save(update_fields=[
                "date_to_return",
                "additional_days",
                "extension_requested",
                "comments"
            ])

    def reject_extension(self):
        if self.additional_days > 0:
            self.additional_days = 0
            self.extension_requested = False
            self.comments = None
            self.save(update_fields=[
                "additional_days",
                "extension_requested",
                "comments"
            ])

    def finish_borrowing(self):
        self.product.change_availability()
        self.delete()


class Breakage(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    product = models.ForeignKey(
        "Product", on_delete=models.PROTECT)
    comments = models.TextField(max_length=200, null=True, blank=True)
    broke_at = models.DateTimeField(auto_now_add=True)
    repaired_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ("user", "product")
        ordering = ["broke_at", "user"]

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.product.set_breakage_reported()
        super().save(*args, **kwargs)

    def send_for_repair(self):
        self.product.increase_times_broken()
        self.product.change_condition()

    def reject_report(self):
        self.product.set_breakage_reported()
        self.delete()

    def mark_repaired(self):
        self.product.change_condition()
        self.delete()
