from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import logging

from base.models import *

User = get_user_model()
logger = logging.getLogger()


class Command(BaseCommand):
    help = "Seeds the database with initial data"

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.WARNING("Trying to seed data..."))
            User.objects.all().delete()
            Category.objects.all().delete()
            Product.objects.all().delete()
            seed(self)
        except Exception as e:
            self.stderr.write(f"Failure while trying to seed data: {str(e)}")
            return

        self.stdout.write(self.style.SUCCESS("Done, data seeded successfully"))


def create_users(self):
    self.stdout.write(self.style.HTTP_INFO("1/4 Creating superuser..."))
    """
    Creating superuser
    """
    User.objects.create_user(
        username="root",
        password="sce123456",
        is_superuser=True,
        is_staff=True,
        is_admin=True,
        is_first_login=False,
    ).save()

    self.stdout.write(self.style.HTTP_INFO("2/4 Creating manager..."))
    """
    Creating manager (מנהל מחסן)
    """
    User.objects.create_user(
        username="manager",
        password="sce123456",
        first_name="Shai",
        last_name="Kohen",
        email="manager_dht@mail.com",
        identity_num="000000000",
        mobile_num="0500000000",
        is_admin=True,
        is_first_login=False,
    ).save()

    self.stdout.write(self.style.HTTP_INFO("3/4 Creating moderator..."))
    """
    Creating moderator
    """
    regular_user_that_will_be_promoted = User.objects.create_user(
        username="moderator",
        password="111111111",
        first_name="Lol",
        last_name="Kek",
        email="mod_dht@mail.com",
        identity_num="111111111",
        role="student",
        mobile_num="0511111111"
    )
    regular_user_that_will_be_promoted.save()
    regular_user_that_will_be_promoted.promote()

    self.stdout.write(self.style.HTTP_INFO("4/4 Creating regular user..."))
    """
    Creating regular user
    """
    User.objects.create_user(
        username="regular_user",
        password="123456789",
        first_name="John",
        last_name="Doe",
        email="regular_user@mail.com",
        identity_num="123456789",
        role="student",
        mobile_num="0523456789"
    ).save()

    self.stdout.write(self.style.HTTP_NOT_MODIFIED("Users created"))


def create_categories(self):
    self.stdout.write(self.style.HTTP_INFO("Creating categories..."))

    cat_names = ["Camera", "Rec", "Apple", "Tripod",
                 "Light", "Cable", "Convertor", "Projector"]
    rec_subcat_names = ["Mic", "PodCast",
                        "Recordings", "Rec Monitor", "Wireless"]

    categories = [Category(name=name) for name in cat_names if name != "Rec"]
    Category.objects.bulk_create(categories)

    rec_category = Category.objects.create(name="Rec")
    rec_subcategories = [Category(name=name, parent=rec_category)
                         for name in rec_subcat_names]
    Category.objects.bulk_create(rec_subcategories)

    self.stdout.write(self.style.HTTP_NOT_MODIFIED("Categories created"))


def create_products(self):
    def stock_num():
        from random import randint
        return randint(1000000000, 9999999999)

    self.stdout.write(self.style.HTTP_INFO("Creating products..."))

    """ categories = {
        "Camera": Camera,
        "Apple": Apple,
        "Tripod": Tripod,
        "Projector": Projector,
        "Cable": Cable,
        "Light": Light,
        "Convertor": Convertor,
    } """

    categories = Category.objects.all().exclude(children__isnull=False)

    for category in categories:
        for i in range(10):
            name = f"{category} – Item {i + 1}"
            Product.objects.create(
                category=category,
                stock_num=stock_num(),
                name=name
            )

    self.stdout.write(self.style.HTTP_NOT_MODIFIED("Products created"))


def seed(self):
    create_users(self)
    create_categories(self)
    create_products(self)
