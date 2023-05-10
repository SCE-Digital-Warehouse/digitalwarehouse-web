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

    path("edit-user/<int:user_id>/", edit_user, name="edit_user"),
    path("delete-user/<int:user_id>/", delete_user, name="delete_user"),
    path("prom-dem-user/<int:user_id>/", prom_dem_user, name="prom_dem_user"),
    path("user/<int:user_id>/", show_user, name="show_user"),
    path("users/", show_users, name="show_users"),

    path("catalog/", catalog, name="catalog"),
    path("personal_det/", personal_det, name="personal_det"),
    path("special_requests/", special_requests, name="special_requests"),
    path("requests/", requests, name="requests"),
    path("statistics/", statistics, name="statistics"),
    path("contact_us/", contact_us, name="contact_us"),

    path("add-category/", add_category, name="add_category"),
    path("category/<int:cat_id>/", show_category, name="show_category"),

    path("add-product/<int:cat_id>/", add_product, name="add_product"),
    path("delete-product/<int:prod_id>/",
         delete_product, name="delete_product"),
    path("edit-product/<int:prod_id>/", edit_product, name="edit_product"),
    # path("bad-product/<int:prod_id>/", bad_product, name="bad_product"),

    path(
        "requests/<int:cat_id>/",
        requests_per_product,
        name="requests_per_product"
    ),
    path("borrowings/<int:cat_id>/", borrowings_per_cat, name="borrowings_per_cat"),

    path(
        "extention-request/<int:borrow_id>/", extention_request, name="extention_req"
    ),
]
