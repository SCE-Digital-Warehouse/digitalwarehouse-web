from django.shortcuts import render, redirect
from django.contrib import messages

def login(request):
    mail = 'pashnikitenko@gmail.com'
    password = '123456'
    if request.method == 'POST':
        m = request.POST.get('email')
        p = request.POST.get('password')
        if m == mail and password == p:
            return redirect('index')
        else:
            messages.error(request, 'Username or password are incorrect!')
    data = {"mail": mail, "password": password}
    return render(request, "base/login.html", data)

def asks(request):
    data = {}
    return render(request, "base/asks.html", data)

def users(request):
    data = {}
    return render(request, "base/users.html", data)

def menu(request):
    data = {}
    return render(request, "base/menu.html", data)

def index(request):
    data = {}
    return render(request, "base/index.html", data)

def personal_det(request):
    return render(request, "base/personal_det.html")

def special_asks(request):
    data = {}
    return render(request, "base/special_asks.html", data)
def queues(requset):
    data = {}
    return render(requset, "base/queues.html", data)
