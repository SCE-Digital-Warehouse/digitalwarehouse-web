from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from base.models import *

User = get_user_model()


class Command(BaseCommand):
    help = "Seeds the database with initial data"

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.WARNING("Trying to seed data..."))
            User.objects.all().delete()
            seed()
        except Exception as e:
            self.stderr.write(f"Failure while trying to seed data: {str(e)}")
            return

        self.stdout.write(self.style.SUCCESS("Done, data seeded successfully"))


def seed():
    """
    Creating superuser
    """
    User.objects.create_user(
        username="root",
        password="sce123456",
        is_superuser=True,
        is_staff=True,
        is_admin=True,
    ).save()

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
        is_admin=True
    ).save()

    """
    Creating moderator
    """
    User.objects.create_user(
        username="moderator",
        password="111111111",
        first_name="Lol",
        last_name="Kek",
        email="mod_dht@mail.com",
        identity_num="111111111",
        role="student",
        mobile_num="0511111111",
        is_mod=True
    ).save()

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
