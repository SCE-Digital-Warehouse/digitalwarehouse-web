from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def login(request):
    return render(request, "base/login.html")

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "base/index.html")
