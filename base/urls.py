from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("home/", views.index, name="index"),
    path("asks/", views.asks, name="asks"),
    path("users/", views.users, name="users"),
    path("menu/", views.menu, name="menu"),
    path("personal_det/", views.personal_det, name="personal_det"),
    path("special_asks/", views.special_asks, name="special_asks"),
    path("queues/", views.queues, name="queues"),
]
