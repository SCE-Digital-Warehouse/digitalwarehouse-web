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
        self.asks_url = reverse("asks")
        self.users_url = reverse("users")
        self.menu_url = reverse("menu")
        self.personal_det_url = reverse("personal_det")
        self.special_asks_url = reverse("special_asks")
        self.queues_url = reverse("queues")
        self.statistics_url = reverse("stat")
        self.connections_url = reverse("connections")

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

    def test_asks_GET(self):
        response = self.client.get(self.asks_url)
        self.assertEquals(response.status_code, 302)

    def test_users_GET(self):
        response = self.client.get(self.users_url)
        self.assertEquals(response.status_code, 302)

    def test_menu_GET(self):
        response = self.client.get(self.menu_url)
        self.assertEquals(response.status_code, 302)

    def test_personal_det_GET(self):
        response = self.client.get(self.personal_det_url)
        self.assertEquals(response.status_code, 302)

    def test_special_asks_GET(self):
        response = self.client.get(self.special_asks_url)
        self.assertEquals(response.status_code, 302)

    def test_queues_GET(self):
        response = self.client.get(self.queues_url)
        self.assertEquals(response.status_code, 302)

    def test_statistics_GET(self):
        response = self.client.get(self.statistics_url)
        self.assertEquals(response.status_code, 302)

    def test_connections_GET(self):
        response = self.client.get(self.connections_url)
        self.assertEquals(response.status_code, 302)
