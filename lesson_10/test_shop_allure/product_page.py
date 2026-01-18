import allure
from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Добавить в корзину товар {item_name}")
    def add_product_cart(self, item_name: str):
        """
        Функция добавления товара в корзину
        :param item_name: - название товара
        """
        self.driver.find_element(By.XPATH, f"//div[text()='{item_name}']/../../..//button").click()

    @allure.step("Перейти в корзину")
    def go_cart(self):
        """
        Функция перехода на страницу Корзина покупателя
        """
        self.driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container').click()
