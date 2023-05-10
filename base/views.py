from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from base.models import *
from django.db.models import F

from config.settings import LOGIN_URL
from .utils import get_user_type
from .forms import *
from .models import *


@login_required(login_url=LOGIN_URL)
def index(request):
    user = request.user
    user_type = get_user_type(request)
    categories = Category.objects.all()
    context = {"user_type": user_type, "categories": categories}
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
    categories = Category.objects.all()
    context = {"user_type": user_type, "categories": categories}
    return render(request, "base/borrowings.html", context)


@login_required(login_url=LOGIN_URL)
def show_users(request):
    user_type = get_user_type(request)
    if user_type == "admin":
        users = User.objects.filter(is_staff=False)
        categories = Category.objects.all()
        context = {
            "user_type": user_type,
            "users": users,
            "categories": categories,
        }
        return render(request, "base/user_manipulation/show_users.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def delete_user(request, user_id):
    user_type = get_user_type(request)
    if user_type == "admin":
        categories = Category.objects.all()
        try:
            user = User.objects.get(pk=user_id)
        except Exception:
            return redirect("show_users", permanent=True)
        if request.method == "POST":
            try:
                user.delete()
            except Exception:
                pass
            finally:
                return redirect("show_users")
        context = {
            "user_type": user_type,
            "user": user,
            "categories": categories,
        }
        return render(request, "base/user_manipulation/delete_user.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def show_user(request, user_id):
    user_type = get_user_type(request)
    categories = Category.objects.all()
    context = {"user_type": user_type, "categories": categories}
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
    categories = Category.objects.all()
    context = {"user_type": user_type, "categories": categories}
    return render(request, "base/catalog.html", context)


@login_required(login_url=LOGIN_URL)
def personal_det(request):
    user_type = get_user_type(request)
    categories = Category.objects.all()
    context = {"user_type": user_type, "categories": categories}
    return render(request, "base/personal_det.html", context)


@login_required(login_url=LOGIN_URL)
def special_requests(request):
    user_type = get_user_type(request)
    categories = Category.objects.all()
    context = {"user_type": user_type, "categories": categories}
    if user_type == "admin":
        return render(request, "base/special_requests.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def requests(request):
    user_type = get_user_type(request)
    categories = Category.objects.all()
    context = {"user_type": user_type, "categories": categories}
    return render(request, "base/requests.html", context)


@login_required(login_url=LOGIN_URL)
def statistics(request):
    user_type = get_user_type(request)
    categories = Category.objects.all()
    total_users = User.objects.count()
    total_mods = Moderator.objects.count()
    total_requests = Request.objects.count()
    total_borrowings = Borrowing.objects.count()
    total_in_repair = Repair.objects.count()
    total_products = Product.objects.count()
    context = {
        "user_type": user_type,
        "total_users": total_users,
        "total_mods": total_mods,
        "total_requests": total_requests,
        "total_borrowings": total_borrowings,
        "total_products": total_products,
        "total_in_repair": total_in_repair,
        "categories": categories
    }
    if user_type == "admin":
        return render(request, "base/statistics.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def contact_us(request):
    user_type = get_user_type(request)
    categories = Category.objects.all()
    context = {"user_type": user_type, "categories": categories}
    return render(request, "base/contact_us.html", context)


@login_required(login_url=LOGIN_URL)
def add_category(request):
    categories = Category.objects.all()
    user_type = get_user_type(request)
    if user_type == "admin":
        if request.method == "POST":
            cat_parent = request.POST.get("cat_parent")
            try:
                if cat_parent != "ללא קטגורית אב":
                    category = Category.objects.create(
                        name=request.POST.get("cat_name"),
                        parent=Category.objects.get(name=cat_parent),
                        image_url=request.POST.get("cat_image")
                    )
                    category.save()
                else:
                    category = Category.objects.create(
                        name=request.POST.get("cat_name"),
                        image_url=request.POST.get("cat_image")
                    )
                    category.save()
            except Exception:
                return redirect("add_category")
        context = {"categories": categories, "user_type": user_type}
        return render(request, "base/category_manipulations/add_category.html", context)
    else:
        return redirect("home")


@login_required(login_url=LOGIN_URL)
def show_category(request, cat_id):
    """Shows all products by specific category."""
    categories = Category.objects.all()
    user_type = get_user_type(request)
    products = Product.objects.all().filter(category_id=cat_id)
    try:
        category = Category.objects.get(pk=cat_id)
    except Exception:
        return redirect("home", permanent=True)
    context = {
        "categories": categories,
        "user_type": user_type,
        "category": category,
        "products": products
    }
    return render(request, "base/category_manipulations/show_category.html", context)


@login_required(login_url=LOGIN_URL)
def add_product(request, cat_id):
    categories = Category.objects.all()
    user_type = get_user_type(request)
    try:
        category = Category.objects.get(pk=cat_id)
    except Exception:
        return redirect("home", permanent=True)
    if user_type == "admin":
        if request.method == "POST":
            try:
                product = Product.objects.create(
                    name=request.POST.get("prod_name"),
                    stock_num=request.POST.get("stock_num"),
                    category=category
                )
                product.save()
            except Exception:
                return redirect("home")
        context = {
            "categories": categories,
            "user_type": user_type,
            "category": category
        }
        return render(request, "base/product_manipulations/add_product.html", context)
    else:
        return redirect("show_category", cat_id)


@login_required(login_url=LOGIN_URL)
def delete_product(request, prod_id):
    categories = Category.objects.all()
    user_type = get_user_type(request)
    product = Product.objects.get(pk=prod_id)
    try:
        category = Category.objects.get(pk=product.category.id)
    except Exception:
        return redirect("home", permanent=True)
    if user_type == "admin":
        if request.method == "POST":
            try:
                product.delete()
            except Exception:
                return redirect("home")
            return redirect("show_category", category.id)
        context = {
            "categories": categories,
            "user_type": user_type,
            "category": category,
            "product": product
        }
        return render(request, "base/product_manipulations/delete_product.html", context)
    else:
        return redirect("show_category", category.id)


@login_required(login_url=LOGIN_URL)
def edit_product(request, prod_id):
    categories = Category.objects.all()
    user_type = get_user_type(request)
    product = Product.objects.get(pk=prod_id)
    try:
        category = Category.objects.get(pk=product.category.id)
    except Exception:
        return redirect("home", permanent=True)
    if user_type == "admin":
        if request.method == "POST":
            cat_parent = request.POST.get("cat_parent")
            try:
                product.delete()
                product = Product.objects.update_or_create(
                    name=request.POST.get("prod_name"),
                    stock_num=request.POST.get("stock_num"),
                    category=Category.objects.get(name=cat_parent)
                )
            except Exception:
                return redirect("home")
            return redirect("show_category", category.id)
        context = {
            "categories": categories,
            "user_type": user_type,
            "category": category,
            "product": product
        }
        return render(request, "base/product_manipulations/edit_product.html", context)
    else:
        return redirect("show_category", category.id)


""" @login_required(login_url=LOGIN_URL)
def bad_product(request, prod_id):
    categories = Category.objects.all()
    user_type = get_user_type(request)
    product = Product.objects.get(pk=prod_id)
    if user_type == "admin":
        try:
            category = Category.objects.get(pk=product.category.id)
        except Exception:
            return redirect("home", permanent=True)
        try:
            product.is_available = False
            product.save()
        except:
            return render("home")
    context = {
        "categories": categories,
        "user_type": user_type,
        "category": category,
        "product": product
    }
    return render(request, "base/category_manipulations/show_category.html", context) """


@login_required(login_url=LOGIN_URL)
def requests_per_product(request, cat_id):
    categories = Category.objects.all()
    user_type = get_user_type(request)
    if user_type == "admin":
        try:
            category = Category.objects.get(pk=cat_id)
        except:
            return render("home")
    context = {
        "categories": categories,
        "user_type": user_type,
        "category": category
    }
    return render(request, "base/requests_per_cat.html", context)


@login_required(login_url=LOGIN_URL)
def borrowings_per_cat(request, cat_id):
    categories = Category.objects.all()
    user_type = get_user_type(request)
    if user_type == "admin":
        try:
            category = Category.objects.get(pk=cat_id)
        except:
            return render("home")
    context = {
        "categories": categories,
        "user_type": user_type,
        "category": category
    }
    return render(request, "base/borrowings_by_cat.html", context)
