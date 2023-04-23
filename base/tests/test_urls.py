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
        url = reverse("asks")
        self.assertEquals(resolve(url).func, asks)

    def test_users_url_is_resolved(self):
        url = reverse("users")
        self.assertEquals(resolve(url).func, users)

    def test_menu_url_is_resolved(self):
        url = reverse("menu")
        self.assertEquals(resolve(url).func, menu)

    def test_personal_det_url_is_resolved(self):
        url = reverse("personal_det")
        self.assertEquals(resolve(url).func, personal_det)

    def test_special_asks_url_is_resolved(self):
        url = reverse("special_asks")
        self.assertEquals(resolve(url).func, special_asks)

    def test_queues_url_is_resolved(self):
        url = reverse("queues")
        self.assertEquals(resolve(url).func, queues)

    def test_stat_url_is_resolved(self):
        url = reverse("stat")
        self.assertEquals(resolve(url).func, statistics)

    def test_connections_url_is_resolved(self):
        url = reverse("connections")
        self.assertEquals(resolve(url).func, connections)
