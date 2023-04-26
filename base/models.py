from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    ROLES = (
        ("student", "סטודנט"),
        ("lecturer", "מרצה"),
        ("manager", "מנהל מחסן")
    )

    identity_num = models.CharField(max_length=9, unique=True, validators=[
        RegexValidator(
            regex=r"[0-9]{9}",
            message="תעודת זהות לא תקינה"
        )
    ])
    role = models.CharField(max_length=15, choices=ROLES)
    mobile_num = models.CharField(max_length=10, unique=True, validators=[
        RegexValidator(
            regex=r"[05][0-9]{8}",
            message="מספר נייד לא חוקי"
        )])
    is_admin = models.BooleanField(default=False)
    is_mod = models.BooleanField(default=False)


class Product():
    stock_num = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)
    in_stock = models.BooleanField(default=True)
    comments = models.TextField(max_length=100)


class Borrow():
    date_borrowed = models.DateTimeField(auto_now_add=True)
    date_to_return = models.DateTimeField()
    returned_at = models.DateTimeField()


class Request():
    date_requested = models.DateTimeField(auto_now_add=True)
    exp_date_to_borrow = models.DateTimeField()
    exp_date_to_return = models.DateTimeField()
    