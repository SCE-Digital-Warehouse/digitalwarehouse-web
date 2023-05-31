# Generated by Django 4.1.7 on 2023-05-31 00:49

import base.utils
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "identity_num",
                    models.CharField(
                        max_length=9,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="תעודת זהות לא תקינה", regex="[0-9]{9}"
                            )
                        ],
                    ),
                ),
                (
                    "mobile_num",
                    models.CharField(
                        max_length=10,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="מספר נייד לא חוקי", regex="[05][0-9]{8}"
                            )
                        ],
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "role",
                    models.CharField(
                        blank=True,
                        choices=[
                            (None, "תבחר/י סוג משתמש"),
                            ("student", "סטודנט"),
                            ("lecturer", "מרצה"),
                        ],
                        max_length=10,
                    ),
                ),
                ("is_first_login", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_mod", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "ordering": ["first_name", "last_name"],
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30, unique=True)),
                ("image_url", models.ImageField(upload_to=base.utils.upload_to_path)),
                ("times_borrowed", models.IntegerField(default=0)),
                ("times_broken", models.IntegerField(default=0)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="base.category",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "categories",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stock_num", models.CharField(max_length=30, unique=True)),
                ("name", models.CharField(max_length=20)),
                ("comments", models.TextField(blank=True, max_length=200, null=True)),
                ("times_borrowed", models.IntegerField(default=0)),
                ("times_broken", models.IntegerField(default=0)),
                ("is_available", models.BooleanField(default=True)),
                ("breakage_reported", models.BooleanField(default=False)),
                ("in_repair", models.BooleanField(default=False)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.category"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Moderator",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        db_column="id",
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("add_product", models.BooleanField(default=True)),
                ("edit_product", models.BooleanField(default=True)),
                ("delete_product", models.BooleanField(default=True)),
                ("accept_request", models.BooleanField(default=True)),
                ("reject_request", models.BooleanField(default=True)),
                ("finish_borrowing", models.BooleanField(default=True)),
                ("mark_repaired", models.BooleanField(default=True)),
                ("promoted_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Request",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comments", models.TextField(blank=True, max_length=200, null=True)),
                ("requested_at", models.DateTimeField(auto_now_add=True)),
                ("exp_date_to_borrow", models.DateTimeField()),
                ("exp_date_to_return", models.DateTimeField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="base.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["requested_at", "user"],
                "get_latest_by": ["requested_at"],
                "unique_together": {("user", "product")},
            },
        ),
        migrations.CreateModel(
            name="Breakage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comments", models.TextField(blank=True, max_length=200, null=True)),
                ("broke_at", models.DateTimeField(auto_now_add=True)),
                ("repaired_at", models.DateTimeField(blank=True, null=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="base.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["broke_at", "user"],
                "unique_together": {("user", "product")},
            },
        ),
        migrations.CreateModel(
            name="Borrowing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comments", models.TextField(blank=True, max_length=200, null=True)),
                ("borrowed_at", models.DateTimeField(auto_now_add=True)),
                ("date_to_return", models.DateTimeField()),
                ("returned_at", models.DateTimeField(blank=True, null=True)),
                ("notified_at", models.DateTimeField(blank=True, null=True)),
                ("extension_requested", models.BooleanField(default=False)),
                ("additional_days", models.PositiveSmallIntegerField(default=0)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="base.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["borrowed_at", "user"],
                "get_latest_by": ["date_to_return"],
                "unique_together": {("user", "product")},
            },
        ),
    ]
