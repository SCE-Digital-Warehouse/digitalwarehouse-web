from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import *


@login_required(login_url="login/")
def index(request):
    context = {}
    if request.session["init_pw_changed"] == True:
        return render(request, "base/index.html", context)
    return redirect("login")


def login_user(request):
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session["init_pw_changed"] = True
            if form.change_password_is_required():
                request.session["init_pw_changed"] = False
                return redirect("set_password")
            return redirect("home")
        else:
            messages.error(request, "שם משתמש/ת ו/או סיסמה לא נכונים")
    else:
        form = LoginUserForm(request)

    context = {"form": form}
    return render(request, "base/login/login.html", context)


@login_required(login_url="login/")
def logout_user(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login/")
def set_password(request: HttpRequest):
    user = request.user
    if request.method == "POST":
        form = PasswordSetForm(user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            request.session["init_pw_changed"] = True
            logout(request)
            return redirect("login")
        else:
            messages.error(request, "סיסמאות לא תואמות")
    else:
        form = PasswordSetForm(user)

    context = {"form": form}
    if request.session["init_pw_changed"] == False:
        return render(request, "base/login/set_password.html", context)
    return redirect("/")


def change_password(request):
    pass


def restore_password(request):
    pass


@login_required(login_url="login/")
def asks(request):
    context = {}
    return render(request, "base/asks.html", context)


@login_required(login_url="login/")
def users(request):
    context = {}
    return render(request, "base/users.html", context)


@login_required(login_url="login/")
def menu(request):
    context = {}
    return render(request, "base/menu.html", context)


@login_required(login_url="login/")
def personal_det(request):
    return render(request, "base/personal_det.html")


@login_required(login_url="login/")
def special_asks(request):
    context = {}
    return render(request, "base/special_asks.html", context)


@login_required(login_url="login/")
def queues(requset):
    context = {}
    return render(requset, "base/queues.html", context)

@login_required(login_url="login/")
def statistics(requset):
    context = {}
    return render(requset, "base/statistika.html", context)

@login_required(login_url="login/")
def connections(requset):
    context = {}
    return render(requset, "base/connections.html", context)
