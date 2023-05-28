from django.urls import path
from django.contrib.auth import views
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("set-password/", set_password, name="set_password"),
    path("change-password/", change_password, name="change_password"),

    path("reset-password/", views.PasswordResetView.as_view(
        template_name="base/reset_password/reset_password.html"), name="reset_password"),
    path("reset-password-sent/", views.PasswordResetDoneView.as_view(
        template_name="base/reset_password/reset_password_sent.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(
        template_name="base/reset_password/reset_password_confirm.html"), name="password_reset_confirm"),
    path("reset-password-complete", views.PasswordResetCompleteView.as_view(
        template_name="base/reset_password/reset_password_complete.html"), name="password_reset_complete"),

    path("users/", users, name="users"),
    path("add-user/", add_user, name="add_user"),
    path("edit-user/<int:user_id>/", edit_user, name="edit_user"),
    path("delete-user/<int:user_id>/", delete_user, name="delete_user"),
    path("prom-dem-user/<int:user_id>/", prom_dem_user, name="prom_dem_user"),
    path("user/<int:user_id>/", user, name="user"),

    path("moderators/", moderators, name="moderators"),
    path("add-moderator/", add_moderator, name="add_moderator"),
    path("edit-moderator/<int:moderator_id>/", edit_moderator, name="edit_moderator"),

    path("personal-details/", personal_details, name="personal_details"),
    path("statistics/", statistics, name="statistics"),
    path("contact-us/", contact_us, name="contact_us"),

    path("category/<int:cat_id>/", category, name="category"),
    path("add-category/", add_category, name="add_category"),
    path("add-product/<int:cat_id>/", add_product, name="add_product"),
    path("edit-product/<int:prod_id>/", edit_product, name="edit_product"),
    path("delete-product/<int:prod_id>/", delete_product, name="delete_product"),
    # path("bad-product/<int:prod_id>/", bad_product, name="bad_product"),

    path("requests/", requests, name="requests"),
    path("requests/<int:category_id>/", requests_per_category, name="requests_per_category"),
    path("request/<int:request_id>/", request, name="request"),
    path("add-request/<int:product_id>/", add_request, name="add_request"),
    path("accept_request/<int:request_id>/", accept_request, name="accept_request"),
    path("reject_request/<int:request_id>/", reject_request, name="reject_request"),

    path("borrowings/", borrowings, name="borrowings"),
    path("borrowings/<int:cat_id>/", borrowings_per_category, name="borrowings_per_category"),
    path("borrowing-extension/<int:borrowing_id>/",
         borrowing_extension, name="borrowing_extension"),
    path("add-borrowing-extension/<int:borrowing_id>/",
         add_borrowing_extension, name="add_borrowing_extension"),
    path("accept-extension/<int:borrowing_id>/", accept_extension, name="accept_extension"),
    path("reject-extension/<int:borrowing_id>/", reject_extension, name="reject_extension"),
    path("finish-borrowing/<int:borrowing_id>/", finish_borrowing, name="finish_borrowing"),

    path("in-repair/", in_repair, name="in_repair"),
    path("in-repair/<int:cat_id>", in_repair_per_category, name="in_repair_per_category"),
    path("breakage/<int:breakage_id>/", breakage, name="breakage"),
    path("mark-repaired/<int:breakage_id>/", mark_repaired, name="mark_repaired"),

]
