import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SauceDemoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def login(self, username="standard_user", password="secret_sauce"):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#user-name'))).send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    def add_products_to_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie'))).click()

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#shopping_cart_container'))).click()

    def checkout(self, first_name, last_name, postal_code):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkout'))).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#first-name'))).send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postal_code)
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def check_total_price(self):
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.summary_total_label"), ""))
        return self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text

@pytest.fixture()
def driver():
    driver_instance = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver_instance
    driver_instance.quit()

def test_full_purchase_flow(driver):
    page = SauceDemoPage(driver)
    page.open()
    # Авторизация
    page.login()
    # Добавляем товары
    page.add_products_to_cart()
    # Переход в корзину
    page.go_to_cart()
    # Оформляем заказ
    page.checkout("Саша", "Майоров", "142615")
    # Проверка стоимости
    total = page.check_total_price()
    assert total == "Total: $58.29"