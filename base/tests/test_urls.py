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

    def test_change_password_url_is_resolved(self):
        url = reverse("change_password")
        self.assertEquals(resolve(url).func, change_password)

    def test_asks_url_is_resolved(self):
        url = reverse("requests")
        self.assertEquals(resolve(url).func, requests)

    def test_users_url_is_resolved(self):
        url = reverse("users")
        self.assertEquals(resolve(url).func, users)

    def test_menu_url_is_resolved(self):
        url = reverse("show_category")
        self.assertEquals(resolve(url).func, category)

    def test_personal_det_url_is_resolved(self):
        url = reverse("personal_det")
        self.assertEquals(resolve(url).func, personal_details)

    def test_special_asks_url_is_resolved(self):
        url = reverse("special_requests")
        self.assertEquals(resolve(url).func, special_requests)

    def test_queues_url_is_resolved(self):
        url = reverse("borrowings")
        self.assertEquals(resolve(url).func, borrowings)

    def test_stat_url_is_resolved(self):
        url = reverse("stat")
        self.assertEquals(resolve(url).func, statistics)

    def test_connections_url_is_resolved(self):
        url = reverse("contact_us")
        self.assertEquals(resolve(url).func, contact_us)

    def test_add_user_url_is_resolved(self):
        url = reverse("add_user")
        self.assertEquals(resolve(url).func, add_user)

    def test_edit_user_url_is_resolved(self):
        url = reverse("edit_user")
        self.assertEquals(resolve(url).func, edit_user)

    def test_delete_user_url_is_resolved(self):
        url = reverse("delete_user")
        self.assertEquals(resolve(url).func, delete_user)

    def test_prom_dem_user_url_is_resolved(self):
        url = reverse("prom_dem_user")
        self.assertEquals(resolve(url).func, prom_dem_user)

    def test_show_user_url_is_resolved(self):
        url = reverse("show_user")
        self.assertEquals(resolve(url).func, user)

    def test_show_users_url_is_resolved(self):
        url = reverse("show_users")
        self.assertEquals(resolve(url).func, users)

    def test_add_category_url_is_resolved(self):
        url = reverse("add_category")
        self.assertEquals(resolve(url).func, add_category)

    def test_show_category_url_is_resolved(self):
        url = reverse("show_category")
        self.assertEquals(resolve(url).func, category)

    def test_add_product_url_is_resolved(self):
        url = reverse("add_product")
        self.assertEquals(resolve(url).func, add_product)

    def test_delete_product_url_is_resolved(self):
        url = reverse("delete_product")
        self.assertEquals(resolve(url).func, delete_product)

    def test_edit_product_url_is_resolved(self):
        url = reverse("edit_product")
        self.assertEquals(resolve(url).func, edit_product)

    def test_requests_per_product_url_is_resolved(self):
        url = reverse("requests_per_product")
        self.assertEquals(resolve(url).func, requests_per_category)

    def test_borrowings_per_cat_url_is_resolved(self):
        url = reverse("borrowings_per_cat")
        self.assertEquals(resolve(url).func, borrowings_per_category)

    def test_add_req_url_is_resolved(self):
        url = reverse("add_req")
        self.assertEquals(resolve(url).func, add_special_request)

    def test_extention_request_is_resolved(self):
        url = reverse("extention_req")
        self.assertEquals(resolve(url).func, borrowing_extention)

    def test_borrow_confirm_is_resolved(self):
        url = reverse("borrow_confirm")
        self.assertEquals(resolve(url).func, borrow_confirm)

    def test_borrow_reject_is_resolved(self):
        url = reverse("borrow_reject")
        self.assertEquals(resolve(url).func, borrow_reject)
