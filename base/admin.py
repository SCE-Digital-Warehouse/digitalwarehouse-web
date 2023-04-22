from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustomUser(UserAdmin):
    list_display = ["id", "identity_num", "username", "email",
                    "first_name", "last_name", "mobile_num", "role", "is_admin", "is_mod", "is_superuser"]
    list_display_links = ["id", "identity_num"]
    search_fields = ["id", "identity_num", "mobile_num"]


admin.site.register(User, CustomUser)
