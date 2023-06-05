from django.test import TestCase, Client
from django.urls import reverse
from base.models import *


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home = reverse("home")
        self.login = reverse("login")
        self.logout = reverse("logout")
        self.set_password = reverse("set_password")
        self.change_password = reverse("change_password")

        self.users = reverse("users")
        self.add_user = reverse("add_user")
        self.add_users = reverse("add_users")
        self.edit_user = reverse("edit_user", args=[1])
        self.delete_user = reverse("delete_user", args=[1])
        self.prom_dem_user = reverse("prom_dem_user", args=[1])

        self.moderators = reverse("moderators")
        self.add_moderator = reverse("add_moderator")
        self.edit_moderator = reverse("edit_moderator", args=[1])

        self.personal_details = reverse("personal_details")
        self.statistics = reverse("statistics")
        self.contact_us = reverse("contact_us")

        self.category = reverse("category", args=[1])
        self.add_category = reverse("add_category")
        self.edit_category = reverse("edit_category", args=[1])
        self.add_product = reverse("add_product", args=[1])
        self.edit_product = reverse("edit_product", args=[1])
        self.delete_product = reverse("delete_product", args=[1])

        self.requests = reverse("requests")
        self.request = reverse("request", args=[1])
        self.requests_per_category = reverse("requests_per_category", args=[1])
        self.add_request = reverse("add_request", args=[1])
        self.cancel_request = reverse("cancel_request", args=[1])
        self.accept_request = reverse("accept_request", args=[1])
        self.reject_request = reverse("reject_request", args=[1])

        self.borrowings = reverse("borrowings")
        self.borrowings_per_category = reverse(
            "borrowings_per_category", args=[1])
        self.borrowing_extension = reverse("borrowing_extension", args=[1])
        self.add_borrowing_extension = reverse(
            "add_borrowing_extension", args=[1])
        self.accept_extension = reverse("accept_extension", args=[1])
        self.reject_extension = reverse("reject_extension", args=[1])
        self.finish_borrowing = reverse("finish_borrowing", args=[1])

        self.breakages = reverse("breakages")
        self.breakage = reverse("breakage", args=[1])
        self.breakages_per_category = reverse(
            "breakages_per_category", args=[1])
        self.send_for_repair = reverse("send_for_repair", args=[1])
        self.report_breakage = reverse("report_breakage", args=[1])
        self.mark_repaired = reverse("mark_repaired", args=[1])
        self.reject_report = reverse("reject_report", args=[1])

    def test_home_GET(self):
        response = self.client.get(self.home)
        self.assertEquals(response.status_code, 302)

    def test_login_GET(self):
        response = self.client.get(self.login)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "base/login/login.html")

    def test_logout_GET(self):
        response = self.client.get(self.logout)
        self.assertEquals(response.status_code, 302)

    def test_set_password_GET(self):
        response = self.client.get(self.set_password)
        self.assertEquals(response.status_code, 302)

    def test_change_password_GET(self):
        response = self.client.get(self.change_password)
        self.assertEquals(response.status_code, 302)

    def test_users_GET(self):
        response = self.client.get(self.users)
        self.assertEquals(response.status_code, 302)

    def test_add_user_GET(self):
        response = self.client.get(self.add_user)
        self.assertEquals(response.status_code, 302)

    def test_add_users_GET(self):
        response = self.client.get(self.add_users)
        self.assertEquals(response.status_code, 302)

    def test_edit_user_GET(self):
        response = self.client.get(self.edit_user)
        self.assertEquals(response.status_code, 302)

    def test_delete_user_GET(self):
        response = self.client.get(self.delete_user)
        self.assertEquals(response.status_code, 302)

    def test_prom_dem_user_GET(self):
        response = self.client.get(self.prom_dem_user)
        self.assertEquals(response.status_code, 302)

    def test_change_password_GET(self):
        response = self.client.get(self.change_password)
        self.assertEquals(response.status_code, 302)

    def test_moderators_GET(self):
        response = self.client.get(self.moderators)
        self.assertEquals(response.status_code, 302)

    def test_add_moderator_GET(self):
        response = self.client.get(self.add_moderator)
        self.assertEquals(response.status_code, 302)

    def test_edit_moderator_GET(self):
        response = self.client.get(self.edit_moderator)
        self.assertEquals(response.status_code, 302)

    def test_statistics_GET(self):
        response = self.client.get(self.statistics)
        self.assertEquals(response.status_code, 302)

    def test_contact_us_GET(self):
        response = self.client.get(self.contact_us)
        self.assertEquals(response.status_code, 302)

    def test_category_GET(self):
        response = self.client.get(self.category)
        self.assertEquals(response.status_code, 302)

    def test_add_category_GET(self):
        response = self.client.get(self.add_category)
        self.assertEquals(response.status_code, 302)

    def test_edit_category_GET(self):
        response = self.client.get(self.edit_category)
        self.assertEquals(response.status_code, 302)

    def test_add_product_GET(self):
        response = self.client.get(self.add_product)
        self.assertEquals(response.status_code, 302)

    def test_edit_product_GET(self):
        response = self.client.get(self.edit_product)
        self.assertEquals(response.status_code, 302)

    def test_delete_product_GET(self):
        response = self.client.get(self.delete_product)
        self.assertEquals(response.status_code, 302)

    def test_requests_GET(self):
        response = self.client.get(self.requests)
        self.assertEquals(response.status_code, 302)

    def test_request_GET(self):
        response = self.client.get(self.request)
        self.assertEquals(response.status_code, 302)

    def test_requests_per_category_GET(self):
        response = self.client.get(self.requests_per_category)
        self.assertEquals(response.status_code, 302)

    def test_add_request_GET(self):
        response = self.client.get(self.add_request)
        self.assertEquals(response.status_code, 302)

    def test_accept_request_GET(self):
        response = self.client.get(self.accept_request)
        self.assertEquals(response.status_code, 302)

    def test_cancel_request_GET(self):
        response = self.client.get(self.cancel_request)
        self.assertEquals(response.status_code, 302)

    def test_reject_request_GET(self):
        response = self.client.get(self.reject_request)
        self.assertEquals(response.status_code, 302)

    def test_borrowings_GET(self):
        response = self.client.get(self.borrowings)
        self.assertEquals(response.status_code, 302)

    def test_borrowings_per_category_GET(self):
        response = self.client.get(self.borrowings_per_category)
        self.assertEquals(response.status_code, 302)

    def test_borrowing_extension_GET(self):
        response = self.client.get(self.borrowing_extension)
        self.assertEquals(response.status_code, 302)

    def test_add_borrowing_extension_GET(self):
        response = self.client.get(self.add_borrowing_extension)
        self.assertEquals(response.status_code, 302)

    def test_accept_extension_GET(self):
        response = self.client.get(self.accept_extension)
        self.assertEquals(response.status_code, 302)

    def test_reject_extension_GET(self):
        response = self.client.get(self.reject_extension)
        self.assertEquals(response.status_code, 302)

    def test_finish_borrowing_GET(self):
        response = self.client.get(self.finish_borrowing)
        self.assertEquals(response.status_code, 302)

    def test_breakages_GET(self):
        response = self.client.get(self.breakages)
        self.assertEquals(response.status_code, 302)

    def test_breakage_GET(self):
        response = self.client.get(self.breakage)
        self.assertEquals(response.status_code, 302)

    def test_breakages_per_category_GET(self):
        response = self.client.get(self.breakages_per_category)
        self.assertEquals(response.status_code, 302)

    def test_report_breakage_GET(self):
        response = self.client.get(self.report_breakage)
        self.assertEquals(response.status_code, 302)

    def test_mark_repaired_GET(self):
        response = self.client.get(self.mark_repaired)
        self.assertEquals(response.status_code, 302)

    def test_reject_report_GET(self):
        response = self.client.get(self.reject_report)
        self.assertEquals(response.status_code, 302)
