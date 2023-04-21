from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("login/", login_user, name="login"),
    path("set-password/", set_password, name="set_password"),
    path("change-password/", change_password, name="change_password"),
]
