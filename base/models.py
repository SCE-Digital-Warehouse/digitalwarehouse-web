from datetime import timedelta
from django.db import models
from django.db.models import F
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.urls import reverse

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
            moderator = Moderator(user=self)
            moderator.save()
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
    borrow_product = models.BooleanField(default=True)
    approve_return = models.BooleanField(default=True)
    approve_request = models.BooleanField(default=True)
    reject_request = models.BooleanField(default=True)
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
            self.product.is_available = False
            self.product.save()
        super().save(*args, **kwargs)


class SpecialRequest(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    product = models.ForeignKey(
        "Product", on_delete=models.PROTECT)
    comments = models.TextField(max_length=200, null=True, blank=True)
    borrowed_at = models.DateTimeField()
    upd_date_to_return = models.DateTimeField()
    additional_days = models.PositiveSmallIntegerField(default=0)

    class Meta:
        unique_together = ("user", "product")
        ordering = ["borrowed_at", "user"]
        get_latest_by = ["borrowed_at"]

    def save(self, *args, **kwargs):
        if self.pk is None:
            if self.additional_days > 0:
                borrowing = self.product.borrowing_set.first()
                if borrowing:
                    self.borrowed_at = borrowing.borrowed_at
                self.upd_date_to_return = borrowing.date_to_return + \
                    timedelta(days=self.additional_days)
        super().save(*args, **kwargs)


class Borrowing(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(
        "Product", on_delete=models.PROTECT)
    borrowed_at = models.DateTimeField(
        auto_now_add=True)
    date_to_return = models.DateTimeField()
    returned_at = models.DateTimeField(blank=True, null=True)
    extension_requested = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "product")
        ordering = ["borrowed_at", "user"]
        get_latest_by = ["date_to_return"]

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.product.increase_times_borrowed()
        super().save(*args, **kwargs)


class Repair(models.Model):
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
            self.product.increase_times_borrowed()
        super().save(*args, **kwargs)
