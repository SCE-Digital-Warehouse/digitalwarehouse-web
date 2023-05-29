from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta

from config.settings import LOGIN_URL
from .utils import get_user_type, get_previous_template
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
            return render(request, "base/panels/user_panel.html", context)
        if (user_type == "moderator"):
            return render(request, "base/panels/moderator_panel.html", context)
        if (user_type == "admin"):
            return render(request, "base/panels/admin_panel.html", context)
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


@login_required(login_url=LOGIN_URL)
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
            user.cancel_first_login()
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
def users(request):
    user_type = get_user_type(request)
    if user_type == "admin":
        categories = Category.objects.all()
        users = User.objects.filter(is_staff=False).exclude(pk=request.user.pk)
        context = {
            "user_type": user_type,
            "users": users,
            "categories": categories,
        }
        return render(request, "base/user_manipulations/users.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def add_user(request):
    user_type = get_user_type(request)
    if user_type == "admin":
        categories = Category.objects.all()
        if request.method == "POST":
            try:
                User.objects.create(
                    identity_num=request.POST.get("identity_num"),
                    first_name=request.POST.get("first_name"),
                    last_name=request.POST.get("last_name"),
                    mobile_num=request.POST.get("mobile_num"),
                    email=request.POST.get("email"),
                    role=request.POST.get("role"),
                    username=request.POST.get("email").split("@")[0],
                    password=request.POST.get("identity_num")
                )
            except Exception:
                pass
            return redirect("users")
        context = {
            "user_type": user_type,
            "categories": categories,
        }
        return render(request, "base/user_manipulations/add_user.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def edit_user(request, user_id):
    user_type = get_user_type(request)
    if user_type == "admin":
        try:
            user = User.objects.get(pk=user_id)
        except Exception:
            return redirect("home")
        categories = Category.objects.all()
        if request.method == "POST":
            user.identity_num = request.POST.get("identity_num")
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.mobile_num = request.POST.get("mobile_num")
            user.email = request.POST.get("email")
            user.role = request.POST.get("role")
            user.username = request.POST.get("email").split("@")[0]
            user.save()
            return redirect("users")
        context = {
            "user_type": user_type,
            "user": user,
            "categories": categories,
        }
        return render(request, "base/user_manipulations/edit_user.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def delete_user(request, user_id):
    user_type = get_user_type(request)
    if user_type == "admin":
        try:
            user = User.objects.get(pk=user_id)
        except Exception:
            return redirect("home")
        categories = Category.objects.all()
        if request.method == "POST":
            previous_template = get_previous_template(
                request.META.get("HTTP_REFERER"))
            try:
                user.delete()
            except Exception:
                pass
            if previous_template == "users":
                return redirect("users")
            return redirect("moderators")
        context = {
            "user_type": user_type,
            "user": user,
            "categories": categories,
        }
        return render(request, "base/user_manipulations/delete_user.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def prom_dem_user(request, user_id):
    user_type = get_user_type(request)
    if user_type == "admin":
        try:
            user = User.objects.get(pk=user_id)
        except Exception:
            return redirect("home")
        previous_template = get_previous_template(
            request.META.get("HTTP_REFERER"))
        if not user.is_mod:
            user.promote()
        else:
            user.demote()
        if previous_template == "users":
            return redirect("users")
        return redirect("moderators")
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def user(request, user_id):
    user_type = get_user_type(request)
    categories = Category.objects.all()
    context = {"user_type": user_type, "categories": categories}
    if user_type == "admin":
        # -------------------- TESTING URL ADDRESSES --------------------
        try:
            user = User.objects.get(pk=user_id)
        except Exception:
            return redirect("home")
        return HttpResponse(f"User's id is {user_id} User's info: {user}")
        # -------------------- TESTING URL ADDRESSES --------------------
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def moderators(request):
    user_type = get_user_type(request)
    if user_type == "admin":
        categories = Category.objects.all()
        moderators = Moderator.objects.all()
        users = User.objects.filter(moderator__in=moderators)
        context = {
            "user_type": user_type,
            "moderators": users,
            "categories": categories,
        }
        return render(request, "base/user_manipulations/moderators.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def add_moderator(request):
    user_type = get_user_type(request)
    if user_type == "admin":
        categories = Category.objects.all()
        creating_moderator = True
        if request.method == "POST":
            try:
                user = User.objects.create(
                    identity_num=request.POST.get("identity_num"),
                    first_name=request.POST.get("first_name"),
                    last_name=request.POST.get("last_name"),
                    mobile_num=request.POST.get("mobile_num"),
                    email=request.POST.get("email"),
                    role=request.POST.get("role"),
                    username=request.POST.get("email").split("@")[0],
                    password=request.POST.get("identity_num")
                )
                moderator = user.promote()
                moderator.add_product = request.POST.get("add_product")
                moderator.edit_product = request.POST.get("edit_product")
                moderator.delete_product = request.POST.get("delete_product")
                moderator.accept_request = request.POST.get("accept_request")
                moderator.reject_request = request.POST.get("reject_request")
                moderator.finish_borrowing = request.POST.get("finish_borrowing")
                moderator.save()
            except Exception:
                pass
            return redirect("moderators")
        context = {
            "user_type": user_type,
            "categories": categories,
            "creating_moderator": creating_moderator
        }
        return render(request, "base/user_manipulations/add_user.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def edit_moderator(request, moderator_id):
    user_type = get_user_type(request)
    if user_type == "admin":
        editing_moderator = True
        try:
            user = User.objects.get(pk=moderator_id)
            moderator = Moderator.objects.get(pk=moderator_id)
        except Exception:
            return redirect("home")
        categories = Category.objects.all()
        if request.method == "POST":
            user.identity_num = request.POST.get("identity_num")
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.mobile_num = request.POST.get("mobile_num")
            user.email = request.POST.get("email")
            user.role = request.POST.get("role")
            user.username = request.POST.get("email").split("@")[0]
            user.save()
            moderator.add_product = request.POST.get("add_product")
            moderator.edit_product = request.POST.get("edit_product")
            moderator.delete_product = request.POST.get("delete_product")
            moderator.accept_request = request.POST.get("accept_request")
            moderator.reject_request = request.POST.get("reject_request")
            moderator.finish_borrowing = request.POST.get("finish_borrowing")
            moderator.save()
            return redirect("moderators")
        context = {
            "user_type": user_type,
            "categories": categories,
            "editing_moderator": editing_moderator,
            "user": user,
            "moderator": moderator
        }
        return render(request, "base/user_manipulations/edit_user.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def personal_details(request):
    user_type = get_user_type(request)
    user = request.user
    categories = Category.objects.all()
    context = {
        "user_type": user_type,
        "user": user,
        "categories": categories
    }
    return render(request, "base/personal_details.html", context)


@login_required(login_url=LOGIN_URL)
def statistics(request):
    user_type = get_user_type(request)
    if user_type == "admin":
        categories = Category.objects.all()
        total_users = User.objects.count()
        total_mods = Moderator.objects.count()
        total_requests = Request.objects.count()
        total_borrowings = Borrowing.objects.count()
        total_in_repair = Breakage.objects.count()
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
        return render(request, "base/statistics.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def contact_us(request):
    user_type = get_user_type(request)
    categories = Category.objects.all()
    context = {"user_type": user_type, "categories": categories}
    return render(request, "base/contact_us.html", context)


@login_required(login_url=LOGIN_URL)
def requests(request):
    user_type = get_user_type(request)
    user = request.user
    categories = Category.objects.all()
    if user_type in ["admin", "moderator"]:
        requests = Request.objects.all()
    else:
        requests = Request.objects.all().filter(user_id=user.pk)
    context = {
        "user_type": user_type,
        "user": user,
        "categories": categories,
        "requests": requests
    }
    return render(request, "base/request_manipulations/requests.html", context)


@login_required(login_url=LOGIN_URL)
def requests_per_category(request, category_id):
    user_type = get_user_type(request)
    user = request.user
    if user_type in ["admin", "moderator"]:
        try:
            category = Category.objects.get(pk=category_id)
        except Exception:
            return redirect("home")
        categories = Category.objects.all()
        requests = Request.objects.filter(product__category=category)
        context = {
            "categories": categories,
            "category": category,
            "user_type": user_type,
            "user": user,
            "requests": requests
        }
        return render(request, "base/request_manipulations/requests.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def request(request, request_id):
    user_type = get_user_type(request)
    if user_type in ["admin", "moderator"]:
        try:
            requezt = Request.objects.get(pk=request_id)
        except Exception:
            return redirect("requests")
        user = request.user
        moderator = getattr(user, "moderator", None)
        mod_accept_request = user_type == "moderator" and \
            moderator is not None and moderator.accept_request
        mod_reject_request = user_type == "moderator" and \
            moderator is not None and moderator.reject_request
        categories = Category.objects.all()
        context = {
            "categories": categories,
            "user_type": user_type,
            "mod_accept_request": mod_accept_request,
            "mod_reject_request": mod_reject_request,
            "requezt": requezt
        }
        return render(request, "base/request_manipulations/request.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def add_request(request, product_id):
    user_type = get_user_type(request)
    if user_type != "admin":
        try:
            product = Product.objects.get(pk=product_id)
        except Exception:
            return redirect("home")
        if not product.is_available:
            return redirect("home")

        categories = Category.objects.all()
        user = request.user

        now = timezone.localtime(timezone.now())
        datetime_format = "%Y-%m-%dT%H:%M"
        init_value = now.strftime(datetime_format)
        init_value2 = (now + timedelta(hours=1)).strftime(datetime_format)
        max_value = (now + timedelta(days=14)).strftime(datetime_format)

        if request.method == "POST":
            try:
                Request.objects.create(
                    user=user,
                    product=product,
                    exp_date_to_borrow=request.POST.get("exp_date_to_borrow"),
                    exp_date_to_return=request.POST.get("exp_date_to_return"),
                    comments=request.POST.get("comments")
                )
            except Exception:
                product.change_availability()
                return redirect("add_request", product_id)
            return redirect("requests")
        context = {
            "user_type": user_type,
            "categories": categories,
            "product": product,
            "init_value": init_value,
            "init_value2": init_value2,
            "max_value": max_value,
            "user_role": user.role
        }
        return render(request, "base/request_manipulations/add_request.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def accept_request(request, request_id):
    user_type = get_user_type(request)
    user = request.user
    if user_type == "admin" or \
            (user_type == "moderator" and user.moderator.accept_request):
        try:
            requezt = Request.objects.get(pk=request_id)
        except Exception:
            return redirect("home")
        requezt.accept_request()
        return redirect("requests")
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def reject_request(request, request_id):
    user_type = get_user_type(request)
    user = request.user
    if user_type == "admin" or \
            (user_type == "moderator" and user.moderator.reject_request):
        try:
            requezt = Request.objects.get(pk=request_id)
        except Exception:
            return redirect("home")
        requezt.reject_request()
        return redirect("requests")
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def borrowings(request):
    user_type = get_user_type(request)
    categories = Category.objects.all()
    user = request.user
    moderator = getattr(user, "moderator", None)
    mod_finish_borrowing = user_type == "moderator" and \
        moderator is not None and moderator.finish_borrowing
    if user_type in ["admin", "moderator"]:
        borrowings = Borrowing.objects.all()
    elif user_type == "user":
        borrowings = Borrowing.objects.all().filter(user_id=user.pk)
    if user_type == "admin":
        for borrowing in borrowings:
            borrowing.notify_user()
    context = {
        "user_type": user_type,
        "user": user,
        "mod_finish_borrowing": mod_finish_borrowing,
        "categories": categories,
        "borrowings": borrowings,
        "now": timezone.now()
    }
    return render(request, "base/borrowing_manipulations/borrowings.html", context)


@login_required(login_url=LOGIN_URL)
def borrowings_per_category(request, cat_id):
    user_type = get_user_type(request)
    if user_type in ["admin", "moderator"]:
        try:
            category = Category.objects.get(pk=cat_id)
        except Exception:
            return redirect("home")
        user = request.user
        categories = Category.objects.all()
        borrowings = Borrowing.objects.filter(product__category=category)
        for borrowing in borrowings:
            borrowing.notify_user()
        context = {
            "categories": categories,
            "category": category,
            "user_type": user_type,
            "user": user,
            "borrowings": borrowings,
            "now": timezone.now()
        }
        return render(request, "base/borrowing_manipulations/borrowings.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def borrowing_extension(request, borrowing_id):
    user_type = get_user_type(request)
    if user_type == "admin":
        try:
            borrowing = Borrowing.objects.get(pk=borrowing_id)
        except Exception:
            return redirect("home")
        categories = Category.objects.all()
        upd_date_to_return = borrowing.date_to_return + \
            timedelta(days=borrowing.additional_days)
        context = {
            "categories": categories,
            "borrowing": borrowing,
            "upd_date_to_return": upd_date_to_return
        }
        return render(request, "base/borrowing_manipulations/borrowing_extension.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def add_borrowing_extension(request, borrowing_id):
    user_type = get_user_type(request)
    if user_type != "admin":
        try:
            borrowing = Borrowing.objects.get(pk=borrowing_id)
        except Exception:
            return redirect("home")
        if borrowing.product.in_repair:
            return redirect("borrowings")
        user = request.user
        categories = Category.objects.all()
        if request.method == "POST":
            additional_days = int(request.POST.get("additional_days"))
            comments = request.POST.get("comments")
            borrowing.request_extension(additional_days, comments)
            return redirect("borrowings")
        context = {
            "categories": categories,
            "user_type": user_type,
            "user": user,
            "borrowing": borrowing,
        }
        return render(request, "base/borrowing_manipulations/add_borrowing_extension.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def accept_extension(request, borrowing_id):
    user_type = get_user_type(request)
    if user_type == "admin":
        try:
            borrowing = Borrowing.objects.get(pk=borrowing_id)
        except Exception:
            return redirect("home")
        borrowing.accept_extension()
        return redirect("borrowings")
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def reject_extension(request, borrowing_id):
    user_type = get_user_type(request)
    if user_type == "admin":
        try:
            borrowing = Borrowing.objects.get(pk=borrowing_id)
        except Exception:
            return redirect("home")
        borrowing.reject_extension()
        return redirect("borrowings")
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def finish_borrowing(request, borrowing_id):
    user_type = get_user_type(request)
    user = request.user
    moderator = getattr(user, "moderator", None)
    mod_finish_borrowing = user_type == "moderator" and \
        moderator is not None and moderator.finish_borrowing
    if user_type == "admin" or mod_finish_borrowing:
        try:
            borrowing = Borrowing.objects.get(pk=borrowing_id)
        except Exception:
            return redirect("home")
        product = borrowing.product
        borrowing.finish_borrowing()
        if product.breakage_reported:
            product.change_availability()
        return redirect("borrowings")
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def category(request, cat_id):
    """Shows all products by specific category."""
    try:
        category = Category.objects.get(pk=cat_id)
    except Exception:
        return redirect("home")
    user_type = get_user_type(request)
    user = request.user
    moderator = getattr(user, "moderator", None)
    mod_add_product = user_type == "moderator" and \
        moderator is not None and moderator.add_product
    mod_edit_product = user_type == "moderator" and \
        moderator is not None and moderator.edit_product
    mod_delete_product = user_type == "moderator" and \
        moderator is not None and moderator.delete_product
    categories = Category.objects.all()
    products = Product.objects.all().filter(category_id=cat_id)
    context = {
        "categories": categories,
        "user_type": user_type,
        "user": user,
        "mod_add_product": mod_add_product,
        "mod_edit_product": mod_edit_product,
        "mod_delete_product": mod_delete_product,
        "category": category,
        "products": products
    }
    return render(request, "base/category_manipulations/category.html", context)


@login_required(login_url=LOGIN_URL)
def add_category(request):
    user_type = get_user_type(request)
    if user_type == "admin":
        categories = Category.objects.all()
        if request.method == "POST":
            cat_parent = request.POST.get("cat_parent")
            try:
                if cat_parent != "no_cat_parent":
                    Category.objects.create(
                        name=request.POST.get("cat_name"),
                        parent=Category.objects.get(name=cat_parent),
                        image_url=request.POST.get("cat_image")
                    )
                else:
                    Category.objects.create(
                        name=request.POST.get("cat_name"),
                        image_url=request.POST.get("cat_image")
                    )
            except Exception:
                return redirect("add_category")
        context = {"categories": categories, "user_type": user_type}
        return render(request, "base/category_manipulations/add_category.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def add_product(request, cat_id):
    user_type = get_user_type(request)
    user = request.user
    if user_type == "admin" or \
            (user_type == "moderator" and user.moderator.add_product):
        try:
            category = Category.objects.get(pk=cat_id)
        except Exception:
            return redirect("home")
        categories = Category.objects.all()
        if request.method == "POST":
            try:
                Product.objects.create(
                    name=request.POST.get("prod_name"),
                    stock_num=request.POST.get("stock_num"),
                    category=category
                )
            except Exception:
                pass
            return redirect("category", cat_id)
        context = {
            "categories": categories,
            "user_type": user_type,
            "category": category
        }
        return render(request, "base/product_manipulations/add_product.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def edit_product(request, prod_id):
    user_type = get_user_type(request)
    user = request.user
    if user_type == "admin" or \
            (user_type == "moderator" and user.moderator.edit_product):
        try:
            product = Product.objects.get(pk=prod_id)
            category = Category.objects.get(pk=product.category.id)
        except Exception:
            return redirect("home")
        categories = Category.objects.all()
        if request.method == "POST":
            cat_parent = request.POST.get("cat_parent")
            product.name = request.POST.get("prod_name")
            product.stock_num = request.POST.get("stock_num")
            product.category = Category.objects.get(pk=cat_parent)
            product.save()
            return redirect("category", category.id)
        context = {
            "categories": categories,
            "user_type": user_type,
            "category": category,
            "product": product
        }
        return render(request, "base/product_manipulations/edit_product.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def delete_product(request, prod_id):
    user_type = get_user_type(request)
    user = request.user
    if user_type == "admin" or \
            (user_type == "moderator" and user.moderator.delete_product):
        try:
            product = Product.objects.get(pk=prod_id)
            category = Category.objects.get(pk=product.category.id)
        except Exception:
            return redirect("home")
        categories = Category.objects.all()
        if request.method == "POST":
            try:
                product.delete()
            except Exception:
                pass
            return redirect("category", category.id)
        context = {
            "categories": categories,
            "user_type": user_type,
            "category": category,
            "product": product
        }
        return render(request, "base/product_manipulations/delete_product.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def breakages(request):
    user_type = get_user_type(request)
    user = request.user
    if user_type in ["admin", "moderator"]:
        categories = Category.objects.all()
        products_in_repair = Breakage.objects.all()
        moderator = getattr(user, "moderator", None)
        mod_mark_repaired = user_type == "moderator" and \
            moderator is not None and moderator.mark_repaired
        context = {
            "user_type": user_type,
            "user": user,
            "mod_mark_repaired": mod_mark_repaired,
            "categories": categories,
            "products_in_repair": products_in_repair
        }
    return render(request, "base/breakage_manipulations/breakages.html", context)


@login_required(login_url=LOGIN_URL)
def breakages_per_category(request, category_id):
    user_type = get_user_type(request)
    if user_type in ["admin", "moderator"]:
        try:
            category = Category.objects.get(pk=category_id)
        except Exception:
            return redirect("home")
        user = request.user
        categories = Category.objects.all()
        products_in_repair = Breakage.objects.filter(product__category=category)
        moderator = getattr(user, "moderator", None)
        mod_mark_repaired = user_type == "moderator" and \
            moderator is not None and moderator.mark_repaired
        context = {
            "categories": categories,
            "category": category,
            "user_type": user_type,
            "user": user,
            "mod_mark_repaired": mod_mark_repaired,
            "products_in_repair": products_in_repair
        }
        return render(request, "base/breakage_manipulations/breakages.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def breakage(request, breakage_id):
    user_type = get_user_type(request)
    if user_type in ["admin", "moderator"]:
        try:
            breakage = Breakage.objects.get(pk=breakage_id)
        except Exception:
            return redirect("breakages")
        user = request.user
        moderator = getattr(user, "moderator", None)
        mod_mark_repaired = user_type == "moderator" and \
            moderator is not None and moderator.mark_repaired
        categories = Category.objects.all()
        context = {
            "categories": categories,
            "user_type": user_type,
            "mod_mark_repaired": mod_mark_repaired,
            "breakage": breakage
        }
        return render(request, "base/breakage_manipulations/breakage.html", context)
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def report_breakage(request, product_id):
    user_type = get_user_type(request)
    try:
        product = Product.objects.get(pk=product_id)
    except Exception:
        return redirect("home")
    if (product.breakage_reported or product.in_repair) or \
            (not product.is_available and user_type == "admin"):
        return redirect("home")
    try:
        borrowing = Borrowing.objects.get(product=product, user=user)
    except Exception:
        pass
    else:
        if borrowing.extension_requested:
            borrowing.reject_extension()
    categories = Category.objects.all()
    user = request.user
    if request.method == "POST":
        breakage = Breakage.objects.create(
            user=user,
            product=product,
            comments=request.POST.get("comments")
        )
        if user_type == "admin":
            breakage.send_for_repair()
            return redirect("category", product.category.pk)
        return redirect("borrowings")
    context = {
        "user_type": user_type,
        "categories": categories,
        "product": product
    }
    return render(request, "base/breakage_manipulations/report_breakage.html", context)


@login_required(login_url=LOGIN_URL)
def reject_report(request, breakage_id):
    user_type = get_user_type(request)
    if user_type == "admin":
        try:
            breakage = Breakage.objects.get(pk=breakage_id)
        except Exception:
            return redirect("home")
        if breakage.product.in_repair:
            return redirect("breakages")
        breakage.reject_report()
        return redirect("breakages")
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def send_for_repair(request, breakage_id):
    user_type = get_user_type(request)
    if user_type == "admin":
        try:
            breakage = Breakage.objects.get(pk=breakage_id)
        except Exception:
            return redirect("home")
        product = breakage.product
        if product.in_repair:
            return redirect("home")
        try:
            borrowing = Borrowing.objects.get(product=product, user=user)
        except Exception:
            pass
        else:
            if borrowing:
                borrowing.reject_extension()
        breakage.send_for_repair()
        return redirect("breakages")
    return redirect("home")


@login_required(login_url=LOGIN_URL)
def mark_repaired(request, breakage_id):
    user_type = get_user_type(request)
    user = request.user
    moderator = getattr(user, "moderator", None)
    mod_mark_repaired = user_type == "moderator" and \
        moderator is not None and moderator.mark_repaired
    if user_type == "admin" or mod_mark_repaired:
        try:
            breakage = Breakage.objects.get(pk=breakage_id)
        except Exception:
            return redirect("home")
        breakage.mark_repaired()
        return redirect("breakages")
    return redirect("home")
