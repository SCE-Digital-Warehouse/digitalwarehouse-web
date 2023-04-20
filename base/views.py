from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginUserForm


@login_required(login_url="/login")
def index(request):
    context = {}
    return render(request, "base/index.html", context)


def login_user(request):
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            # TODO: check if it is the 1st time the user logs in, if so -> redirect(change_pw)
            user = form.get_user()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "שם משתמש/ת ו/או סיסמה לא נכונים")
    else:
        form = LoginUserForm(request)

    context = {"form": form}
    return render(request, "base/login/login.html", context)


def restore_password(request):
    pass

def change_password(request: HttpRequest):
    return HttpResponse("change-password")
