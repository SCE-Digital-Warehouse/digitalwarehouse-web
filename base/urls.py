from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("set-password/", set_password, name="set_password"),
    path("reset-password/", reset_password, name="reset_password"),
    path("change-password/", change_password, name="change_password"),
    path("asks/", asks, name="asks"),
    path("users/", users, name="users"),
    path("menu/", menu, name="menu"),
    path("personal-det/", personal_det, name="personal_det"),
    path("special-asks/", special_asks, name="special_asks"),
    path("queues/", queues, name="queues"),
    path("statistic/", statistics, name="stat"),

]
