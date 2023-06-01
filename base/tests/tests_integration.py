import time
from django.utils import timezone
from datetime import timedelta
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ALoginFormTest(LiveServerTestCase):
    def test(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/login/")

        wait = WebDriverWait(driver, 10)

        username = wait.until(
            EC.presence_of_element_located((By.NAME, "username")))
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.ID, "submit")

        username.send_keys("manager_dht")
        password.send_keys("sce123456")

        time.sleep(3)

        submit.send_keys(Keys.RETURN)

        time.sleep(3)

        moderators_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='home-card']"))
        )
        assert moderators_button.is_displayed()

        driver.get("http://127.0.0.1:8000/logout/")


class BRequestTest(LiveServerTestCase):
    def test(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/login/")

        wait = WebDriverWait(driver, 10)

        username = wait.until(
            EC.presence_of_element_located((By.NAME, "username")))
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.ID, "submit")

        username.send_keys("regular_user")
        password.send_keys("sce123456")

        time.sleep(3)

        submit.send_keys(Keys.RETURN)

        time.sleep(3)

        new_password1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "id_new_password1"))
        )
        new_password2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "id_new_password2"))
        )

        form = driver.find_element(By.CSS_SELECTOR, 'form[method="post"]')

        new_password1.send_keys("droch123456")
        new_password2.send_keys("droch123456")

        time.sleep(3)

        form.submit()

        username = wait.until(
            EC.presence_of_element_located((By.NAME, "username")))
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.ID, "submit")

        username.send_keys("regular_user")
        password.send_keys("droch123456")

        time.sleep(3)

        submit.send_keys(Keys.RETURN)

        time.sleep(3)

        driver.get("http://127.0.0.1:8000/category/1/")

        time.sleep(3)

        driver.get("http://127.0.0.1:8000/add-request/1/")

        time.sleep(3)

        exp_date_to_borrow = wait.until(
            EC.presence_of_element_located((By.NAME, "exp_date_to_borrow")))
        exp_date_to_return = driver.find_element(By.NAME, "exp_date_to_return")
        submit = driver.find_element(By.ID, "submit")
        form = driver.find_element(By.CSS_SELECTOR, 'form[method="post"]')

        now = timezone.localtime(timezone.now())
        datetime_format = "%Y-%m-%dT%H:%M"

        exp_date_to_borrow.send_keys(
            (now + timedelta(days=1)).strftime(datetime_format))
        exp_date_to_return.send_keys(
            (now + timedelta(days=2)).strftime(datetime_format))

        form.submit()

        time.sleep(3)

        driver.get("http://127.0.0.1:8000/logout/")


class ConfirmRequestTest(LiveServerTestCase):
    def test(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/login/")

        wait = WebDriverWait(driver, 10)

        username = wait.until(
            EC.presence_of_element_located((By.NAME, "username")))
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.ID, "submit")

        username.send_keys("manager_dht")
        password.send_keys("sce123456")

        time.sleep(3)

        submit.send_keys(Keys.RETURN)

        time.sleep(3)

        driver.get("http://127.0.0.1:8000/requests/")

        time.sleep(3)

        driver.get("http://127.0.0.1:8000/request/1/")

        time.sleep(3)

        driver.get("http://127.0.0.1:8000/accept_request/1/")

        time.sleep(3)

        driver.get("http://127.0.0.1:8000/logout/")
        driver.get("http://127.0.0.1:8000/login/")

        username = wait.until(
            EC.presence_of_element_located((By.NAME, "username")))
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.ID, "submit")

        username.send_keys("regular_user")
        password.send_keys("droch123456")

        time.sleep(3)

        submit.send_keys(Keys.RETURN)

        time.sleep(3)

        driver.get("http://127.0.0.1:8000/borrowings/")

        time.sleep(3)

        table = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='borrowings-page-admin']"))
        )
        assert table.is_displayed()

        driver.get("http://127.0.0.1:8000/logout/")
