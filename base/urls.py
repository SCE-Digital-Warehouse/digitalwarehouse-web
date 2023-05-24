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
        name="reset_password"
    ),
    path(
        "reset-password-sent/",
        views.PasswordResetDoneView.as_view(
            template_name="base/reset_password/reset_password_sent.html"),
        name="password_reset_done"
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(
            template_name="base/reset_password/reset_password_confirm.html"),
        name="password_reset_confirm"
    ),
    path(
        "reset-password-complete",
        views.PasswordResetCompleteView.as_view(
            template_name="base/reset_password/reset_password_complete.html"),
        name="password_reset_complete"
    ),

    path("change-password/", change_password, name="change_password"),

    path("add-user/", add_user, name="add_user"),
    path("edit-user/<int:user_id>/", edit_user, name="edit_user"),
    path("delete-user/<int:user_id>/", delete_user, name="delete_user"),
    path("prom-dem-user/<int:user_id>/", prom_dem_user, name="prom_dem_user"),
    path("users/", users, name="users"),
    path("user/<int:user_id>/", user, name="user"),

    path("personal-details/", personal_details, name="personal_details"),
    path("borrowings/", borrowings, name="borrowings"),
    path("requests/", requests, name="requests"),
    path("special-requests/", special_requests, name="special_requests"),
    path("statistics/", statistics, name="statistics"),
    path("contact-us/", contact_us, name="contact_us"),

    path("add-category/", add_category, name="add_category"),
    path("category/<int:cat_id>/", category, name="category"),

    path("add-product/<int:cat_id>/", add_product, name="add_product"),
    path(
        "delete-product/<int:prod_id>/",
        delete_product,
        name="delete_product"
    ),
    path("edit-product/<int:prod_id>/", edit_product, name="edit_product"),
    # path("bad-product/<int:prod_id>/", bad_product, name="bad_product"),

    path(
        "requests/<int:cat_id>/",
        requests_per_category,
        name="requests_per_product"
    ),
    path(
        "borrowings/<int:cat_id>/",
        borrowings_per_category,
        name="borrowings_per_category"
    ),

    path(
        "borrowing-extension/<int:borrowing_id>/",
        borrowing_extension,
        name="borrowing_extension"
    ),
    path(
        "add-borrowing-extension/<int:borrowing_id>/",
        add_borrowing_extension,
        name="add_borrowing_extension"
    ),
    path(
        "accept-extension/<int:borrow_id>/",
        accept_extension,
        name="accept_extension"
    ),
    path(
        "reject-extension/<int:borrow_id>/",
        reject_extension,
        name="reject_extension"
    )

]
