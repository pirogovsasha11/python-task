import allure
from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Нажать кнопку Checkout")
    def checkout(self):
        """
        Функция нажатия кнопки Checkout на странице Корзина
        """
        self.driver.find_element(By.ID, "checkout").click()