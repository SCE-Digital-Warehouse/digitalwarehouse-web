from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.urls import *
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse("home")
        self.assertEquals(resolve(url).func, index)

    def test_login_url_is_resolved(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func, login_user)

    def test_logout_url_is_resolved(self):
        url = reverse("logout")
        self.assertEquals(resolve(url).func, logout_user)

    def test_set_password_url_is_resolved(self):
        url = reverse("set_password")
        self.assertEquals(resolve(url).func, set_password)

    def test_change_password_url_is_resolved(self):
        url = reverse("change_password")
        self.assertEquals(resolve(url).func, change_password)

    def test_reset_password_url_is_resolved(self):
        url = reverse("reset_password")
        self.assertEquals(resolve(url).func.view_class, PasswordResetView)

    def test_password_reset_done_url_is_resolved(self):
        url = reverse("password_reset_done")
        self.assertEquals(resolve(url).func.view_class, PasswordResetDoneView)

    def test_password_reset_complete_url_is_resolved(self):
        url = reverse("password_reset_complete")
        self.assertEquals(resolve(url).func.view_class,
                          PasswordResetCompleteView)

    def test_users_url_is_resolved(self):
        url = reverse("users")
        self.assertEquals(resolve(url).func, users)

    def test_add_user_url_is_resolved(self):
        url = reverse("add_user")
        self.assertEquals(resolve(url).func, add_user)

    def test_add_users_url_is_resolved(self):
        url = reverse("add_users")
        self.assertEquals(resolve(url).func, add_users)

    def test_edit_user_url_is_resolved(self):
        user_id = 1
        url = reverse("edit_user", args=[user_id])
        self.assertEquals(resolve(url).func, edit_user)

    def test_delete_user_url_is_resolved(self):
        user_id = 1
        url = reverse("delete_user", args=[user_id])
        self.assertEquals(resolve(url).func, delete_user)

    def test_prom_dem_user_url_is_resolved(self):
        user_id = 1
        url = reverse("prom_dem_user", args=[user_id])
        self.assertEquals(resolve(url).func, prom_dem_user)

    def test_moderators_url_is_resolved(self):
        url = reverse("moderators")
        self.assertEquals(resolve(url).func, moderators)

    def test_add_moderator_url_is_resolved(self):
        url = reverse("add_moderator")
        self.assertEquals(resolve(url).func, add_moderator)

    def test_edit_moderator_url_is_resolved(self):
        moderator_id = 1
        url = reverse("edit_moderator", args=[moderator_id])
        self.assertEquals(resolve(url).func, edit_moderator)

    def test_personal_details_url_is_resolved(self):
        url = reverse("personal_details")
        self.assertEquals(resolve(url).func, personal_details)

    def test_statistics_url_is_resolved(self):
        url = reverse("statistics")
        self.assertEquals(resolve(url).func, statistics)

    def test_contact_us_url_is_resolved(self):
        url = reverse("contact_us")
        self.assertEquals(resolve(url).func, contact_us)

    def test_category_url_is_resolved(self):
        cat_id = 1
        url = reverse("category", args=[cat_id])
        self.assertEquals(resolve(url).func, category)

    def test_add_category_url_is_resolved(self):
        url = reverse("add_category")
        self.assertEquals(resolve(url).func, add_category)

    def test_edit_category_url_is_resolved(self):
        cat_id = 1
        url = reverse("edit_category", args=[cat_id])
        self.assertEquals(resolve(url).func, edit_category)

    def test_add_product_url_is_resolved(self):
        cat_id = 1
        url = reverse("add_product", args=[cat_id])
        self.assertEquals(resolve(url).func, add_product)

    def test_edit_product_url_is_resolved(self):
        prod_id = 1
        url = reverse("edit_product", args=[prod_id])
        self.assertEquals(resolve(url).func, edit_product)

    def test_delete_product_url_is_resolved(self):
        prod_id = 1
        url = reverse("delete_product", args=[prod_id])
        self.assertEquals(resolve(url).func, delete_product)

    def test_requests_url_is_resolved(self):
        url = reverse("requests")
        self.assertEquals(resolve(url).func, requests)

    def test_requests_per_category_url_is_resolved(self):
        category_id = 1
        url = reverse("requests_per_category", args=[category_id])
        self.assertEquals(resolve(url).func, requests_per_category)

    def test_request_url_is_resolved(self):
        request_id = 1
        url = reverse("request", args=[request_id])
        self.assertEquals(resolve(url).func, request)

    def test_add_request_url_is_resolved(self):
        product_id = 1
        url = reverse("add_request", args=[product_id])
        self.assertEquals(resolve(url).func, add_request)

    def test_accept_request_url_is_resolved(self):
        request_id = 1
        url = reverse("accept_request", args=[request_id])
        self.assertEquals(resolve(url).func, accept_request)

    def test_cancel_request_is_resolved(self):
        request_id = 1
        url = reverse("cancel_request", args=[request_id])
        self.assertEquals(resolve(url).func, cancel_request)

    def test_reject_request_url_is_resolved(self):
        request_id = 1
        url = reverse("reject_request", args=[request_id])
        self.assertEquals(resolve(url).func, reject_request)

    def test_borrowings_url_is_resolved(self):
        url = reverse("borrowings")
        self.assertEquals(resolve(url).func, borrowings)

    def test_borrowings_per_category_url_is_resolved(self):
        cat_id = 1
        url = reverse("borrowings_per_category", args=[cat_id])
        self.assertEquals(resolve(url).func, borrowings_per_category)

    def test_borrowing_extension_url_is_resolved(self):
        borrowing_id = 1
        url = reverse("borrowing_extension", args=[borrowing_id])
        self.assertEquals(resolve(url).func, borrowing_extension)

    def test_add_borrowing_extension_url_is_resolved(self):
        borrowing_id = 1
        url = reverse("add_borrowing_extension", args=[borrowing_id])
        self.assertEquals(resolve(url).func, add_borrowing_extension)

    def test_accept_extension_is_resolved(self):
        borrowing_id = 1
        url = reverse("accept_extension", args=[borrowing_id])
        self.assertEquals(resolve(url).func, accept_extension)

    def test_reject_extension_is_resolved(self):
        borrowing_id = 1
        url = reverse("reject_extension", args=[borrowing_id])
        self.assertEquals(resolve(url).func, reject_extension)

    def test_finish_borrowing_is_resolved(self):
        borrowing_id = 1
        url = reverse("finish_borrowing", args=[borrowing_id])
        self.assertEquals(resolve(url).func, finish_borrowing)

    def test_breakages_is_resolved(self):
        url = reverse("breakages")
        self.assertEquals(resolve(url).func, breakages)

    def test_breakages_per_category_is_resolved(self):
        category_id = 1
        url = reverse("breakages_per_category", args=[category_id])
        self.assertEquals(resolve(url).func, breakages_per_category)

    def test_breakage_is_resolved(self):
        breakage_id = 1
        url = reverse("breakage", args=[breakage_id])
        self.assertEquals(resolve(url).func, breakage)

    def test_send_for_repair_is_resolved(self):
        breakage_id = 1
        url = reverse("send_for_repair", args=[breakage_id])
        self.assertEquals(resolve(url).func, send_for_repair)

    def test_report_breakage_is_resolved(self):
        product_id = 1
        url = reverse("report_breakage", args=[product_id])
        self.assertEquals(resolve(url).func, report_breakage)

    def test_mark_repaired_is_resolved(self):
        breakage_id = 1
        url = reverse("mark_repaired", args=[breakage_id])
        self.assertEquals(resolve(url).func, mark_repaired)

    def test_reject_report_is_resolved(self):
        breakage_id = 1
        url = reverse("reject_report", args=[breakage_id])
        self.assertEquals(resolve(url).func, reject_report)
