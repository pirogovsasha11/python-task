import allure
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Авторизоваться как пользователь {username}")
    def username(self, username: str):
        """
        Функция авторизации пользователя, ввода имени
        :param username: - имя пользователя
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    @allure.step("Ввести пароль {password}")
    def password(self, password: str):
        """
         Функция авторизации пользователя, ввода пароля
        :param password: - пароль пользователя
        """
        self.driver.find_element(By.ID, "password").send_keys(password)

    @allure.step("Нажать кнопку LOGIN")
    def click_button(self):
        """
        Функция нажатия кнопки LOGIN
        """
        self.driver.find_element(By.ID, "login-button").click()
