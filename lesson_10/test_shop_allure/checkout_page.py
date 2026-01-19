import allure
from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ввести данные в поле имя {value}")
    def first_name(self,value: str):
        """
        Функция ввода имени
        :param value: str - имя пользователя
        """
        self.driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(value)

    @allure.step("Ввести данные в поле фамилия {value}")
    def last_name(self,value: str):
        """
        Функция ввода фамилии
        :param value: str - фамилия пользователя
        """
        self.driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(value)

    @allure.step("Ввести данные в поле почтовый индекс {value}")
    def postal_code(self,value: str):
        """
        Функция ввода почтового индекса
        :param value: str - почтовый индекс пользователя
        """
        self.driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(value)

    @allure.step("Нажать кнопку CONTINUE")
    def  click_continue(self):
        """
        Функция нажатия кнопки CONTINUE для продолжения покупки товара
        """
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()

    @allure.step("Прочитать со страницы итоговую стоимость")
    def check_total_price(self):
        """
        Функция чтения итоговой стоимости корзины покупателя
        """
        return self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
