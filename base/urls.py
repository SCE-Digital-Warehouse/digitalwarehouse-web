from re import template
from urllib import request
from django.urls import path
from django.contrib.auth import views
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("set-password/", set_password, name="set_password"),

    path(
        "reset-password/",
        views.PasswordResetView.as_view(
            template_name="base/reset_password/reset_password.html"),
        name="reset_password"),
    path(
        "reset-password-sent/",
        views.PasswordResetDoneView.as_view(
            template_name="base/reset_password/reset_password_sent.html"),
        name="password_reset_done"),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(
            template_name="base/reset_password/reset_password_confirm.html"),
        name="password_reset_confirm"),
    path(
        "reset-password-complete",
        views.PasswordResetCompleteView.as_view(
            template_name="base/reset_password/reset_password_complete.html"),
        name="password_reset_complete"),

    path("change-password/", change_password, name="change_password"),
    path("borrowings/", borrowings, name="borrowings"),
    path("users/", users, name="users"),
    path("user/<int:user_id>/", show_user, name="show_user"),
    path("catalog/", catalog, name="catalog"),
    path("personal_det/", personal_det, name="personal_det"),
    path("special_requests/", special_requests, name="special_requests"),
    path("requests/", requests, name="requests"),
    path("statistics/", statistics, name="statistics"),
    path("contact_us/", contact_us, name="contact_us"),

    path("add-category/", add_category, name="add_category"),
    path("category/<int:cat_id>/", show_category, name="show_category"),

    path("add-product/<int:cat_id>/", add_product, name="add_product"),
    path("delete-product/<int:prod_id>/", delete_product, name="delete_product"),
    path("edit-product/<int:prod_id>/", edit_product, name="edit_product"),
    path("bad-product/<int:prod_id>/", bad_product, name="bad_product"),

    path("requests/<int:prod_id>/", requests_by_prod, name="requests_by_prod"),
    path("borrowings/<int:prod_id>/", borrowings_by_prod, name="borrowings_by_prod")
]
