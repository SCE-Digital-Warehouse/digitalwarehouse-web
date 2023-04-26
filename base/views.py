from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .utils import get_user_type
from .forms import *


@login_required(login_url="login/")
def index(request):
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    if request.session.get("init_pw_changed") == True:
        if (user_type == "user"):
            return HttpResponse("User Panel is base/user_panel.html")
            # return render(request, "base/user_panel.html", context)
        if (user_type == "moderator"):
            return HttpResponse("Moderator Panel is base/moderator_panel.html")
            # return render(request, "base/moderator_panel.html", context)
        if (user_type == "admin"):
            return render(request, "base/admin_panel.html", context)
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


def logout_user(request):
    logout(request)
    return redirect("login")


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
    if request.session.get("init_pw_changed") == False:
        return render(request, "base/login/set_password.html", context)
    return redirect("/")


def change_password(request):
    pass


@login_required(login_url="login/")
def borrowings(request):
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    if user_type is not "admin":
        return render(request, "base/borrowings.html", context)
    return redirect("/")


@login_required(login_url="login/")
def users(request):
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    if user_type == "admin":
        return render(request, "base/users.html", context)
    return redirect("/")


@login_required(login_url="login/")
def catalog(request):
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    return render(request, "base/catalog.html", context)


@login_required(login_url="login/")
def personal_det(request):
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    return render(request, "base/personal_det.html", context)


@login_required(login_url="login/")
def special_requests(request):
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    if user_type == "admin":
        return render(request, "base/special_requests.html", context)
    return redirect("/")


@login_required(login_url="login/")
def requests(request):
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    return render(request, "base/requests.html", context)


@login_required(login_url="login/")
def statistics(request):
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    if user_type == "admin":
        return render(request, "base/statistics.html", context)
    return redirect("/")


@login_required(login_url="login/")
def contact_us(request):
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    return render(request, "base/contact_us.html", context)
