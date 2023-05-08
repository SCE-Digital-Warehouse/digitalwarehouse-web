from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from config.settings import LOGIN_URL
from .utils import get_user_type
from .forms import *


@login_required(login_url=LOGIN_URL)
def index(request):
    user = request.user
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    if not user.is_first_login:
        if (user_type == "user"):
            return render(request, "base/user_panel.html", context)
        if (user_type == "moderator"):
            return HttpResponse("Moderator Panel is base/moderator_panel.html")
        if (user_type == "admin"):
            return render(request, "base/admin_panel.html", context)
    return redirect("set_password")


def login_user(request):
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_first_login:
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


@login_required(login_url=LOGIN_URL)
def set_password(request):
    user = request.user
    if request.method == "POST":
        form = PasswordSetForm(user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            user.is_first_login = False
            user.save(update_fields=["is_first_login"])
            logout(request)
            return redirect("login")
        else:
            messages.error(request, "סיסמאות לא תואמות")
    else:
        form = PasswordSetForm(user)

    context = {"form": form}
    if user.is_first_login:
        return render(request, "base/login/set_password.html", context)
    return redirect("home")


def change_password(request):
    pass


@login_required(login_url=LOGIN_URL)
def borrowings(request):
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    return render(request, "base/borrowings.html", context)


@login_required(login_url=LOGIN_URL)
def users(request):
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    if user_type == "admin":
        return render(request, "base/users.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def show_user(request, user_id):
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    if user_type == "admin":
        # -------------------- TESTING URL ADDRESSES --------------------
        try:
            user = User.objects.get(pk=user_id)
        except Exception:
            return redirect("home", permanent=True)
        return HttpResponse(f"User's id is {user_id} User's info: {user}")
        # -------------------- TESTING URL ADDRESSES --------------------
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def catalog(request):
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    return render(request, "base/catalog.html", context)


@login_required(login_url=LOGIN_URL)
def personal_det(request):
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    return render(request, "base/personal_det.html", context)


@login_required(login_url=LOGIN_URL)
def special_requests(request):
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    if user_type == "admin":
        return render(request, "base/special_requests.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def requests(request):
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    return render(request, "base/requests.html", context)


@login_required(login_url=LOGIN_URL)
def statistics(request):
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    if user_type == "admin":
        return render(request, "base/statistics.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def contact_us(request):
    user_type = get_user_type(request)
    context = {"user_type": user_type}
    return render(request, "base/contact_us.html", context)
