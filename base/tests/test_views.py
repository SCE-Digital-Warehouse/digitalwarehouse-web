from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from base.models import *


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse("login")
        self.home_url = reverse("home")
        self.logout_url = reverse("logout")
        self.set_password_url = reverse("set_password")
        self.borrowings_url = reverse("borrowings")
        self.users_url = reverse("users")
        self.show_category_url = reverse("show_category")
        self.personal_det_url = reverse("personal_det")
        self.special_requests_url = reverse("special_requests")
        self.requests_url = reverse("requests")
        self.statistics_url = reverse("stat")
        self.contact_us_url = reverse("contact_us")

        self.add_user_url = reverse("add_user")
        self.edit_user_url = reverse("edit_user")
        self.delete_user_url = reverse("delete_user")
        self.prom_dem_user = reverse("prom_dem_user")
        self.show_user = reverse("show_user")
        self.show_users = reverse("show_users")
        self.add_category = reverse("add_category")
        self.show_category = reverse("show_category")
        self.add_product = reverse("add_product")
        self.delete_product = reverse("delete_product")
        self.edit_product = reverse("edit_product")
        self.requests_per_product = reverse("requests_per_product")
        self.borrowings_per_cat = reverse("borrowings_per_cat")
        self.add_req = reverse("add_req")
        self.extention_req = reverse("extention_req")
        self.borrow_confirm = reverse("borrow_confirm")
        self.borrow_reject = reverse("borrow_reject")


    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 302)

    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "base/login/login.html")

    def test_logout_GET(self):
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code, 302)

    def test_set_password_GET(self):
        response = self.client.get(self.set_password_url)
        self.assertEquals(response.status_code, 302)

    def test_borrowings_GET(self):
        response = self.client.get(self.borrowings_url)
        self.assertEquals(response.status_code, 302)

    def test_users_GET(self):
        response = self.client.get(self.users_url)
        self.assertEquals(response.status_code, 302)

    def test_show_category_GET(self):
        response = self.client.get(self.show_category_url)
        self.assertEquals(response.status_code, 302)

    def test_personal_det_GET(self):
        response = self.client.get(self.personal_det_url)
        self.assertEquals(response.status_code, 302)

    def test_special_requests_GET(self):
        response = self.client.get(self.special_requests_url)
        self.assertEquals(response.status_code, 302)

    def test_requests_GET(self):
        response = self.client.get(self.requests_url)
        self.assertEquals(response.status_code, 302)

    def test_statistics_GET(self):
        response = self.client.get(self.statistics_url)
        self.assertEquals(response.status_code, 302)

    def test_cantact_us_GET(self):
        response = self.client.get(self.contact_us_url)
        self.assertEquals(response.status_code, 302)

    def test_add_user_GET(self):
        response = self.client.get(self.add_user_url)
        self.assertEquals(response.status_code, 302)

    def test_edit_user_GET(self):
        response = self.client.get(self.edit_user_url)
        self.assertEquals(response.status_code, 302)

    def test_delete_user_GET(self):
        response = self.client.get(self.delete_user_url)
        self.assertEquals(response.status_code, 302)

    def test_prom_dem_user_GET(self):
        response = self.client.get(self.prom_dem_user)
        self.assertEquals(response.status_code, 302)

    def test_show_user_GET(self):
        response = self.client.get(self.show_user)
        self.assertEquals(response.status_code, 302)

    def test_show_users_GET(self):
        response = self.client.get(self.show_users)
        self.assertEquals(response.status_code, 302)
    def test_add_category_GET(self):
        response = self.client.get(self.add_category)
        self.assertEquals(response.status_code, 302)

    def test_show_category_GET(self):
        response = self.client.get(self.show_category)
        self.assertEquals(response.status_code, 302)

    def test_add_product_GET(self):
        response = self.client.get(self.add_product)
        self.assertEquals(response.status_code, 302)

    def test_delete_product_GET(self):
        response = self.client.get(self.delete_product)
        self.assertEquals(response.status_code, 302)

    def test_edit_product_GET(self):
        response = self.client.get(self.edit_product)
        self.assertEquals(response.status_code, 302)

    def test_requests_per_product_GET(self):
        response = self.client.get(self.requests_per_product)
        self.assertEquals(response.status_code, 302)

    def test_borrowings_per_cat_GET(self):
        response = self.client.get(self.borrowings_per_cat)
        self.assertEquals(response.status_code, 302)

    def test_add_req_GET(self):
        response = self.client.get(self.add_req)
        self.assertEquals(response.status_code, 302)

    def test_extention_req_GET(self):
        response = self.client.get(self.extention_req)
        self.assertEquals(response.status_code, 302)

    def test_borrow_confirm_GET(self):
        response = self.client.get(self.borrow_confirm)
        self.assertEquals(response.status_code, 302)

    def test_borrow_reject_GET(self):
        response = self.client.get(self.borrow_reject)
        self.assertEquals(response.status_code, 302)
