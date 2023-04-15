from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("home/", views.index, name="index"),
    path("asks/", views.asks, name="asks"),
    path("users/", views.users, name="users"),

]
