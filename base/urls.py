from django.urls import path
from .views import *

urlpatterns = [
    path("", login, name="login"), # http://127.0.0.1:8000/
    path("home/", index, name="index"), # http://127.0.0.1:8000/home/
    path("about/", about, name="about"), # http://127.0.0.1:8000/about/
]
