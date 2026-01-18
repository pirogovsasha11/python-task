import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 46)

    @allure.step("Открыть страницу сайта калькулятора.")
    def open(self):
        """Открытие страницы калькулятора"""
        self.driver.get(
                "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

    @allure.step("Установить задержку {delay} секунд")
    def set_delay(self, delay: int):
        """
        Устанавливает задержку для выполнения операций на калькуляторе
        :param delay: int - время задержки в секундах
        """
        with allure.step("Находим поле ввода задержки"):
            delay_input = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        with allure.step("Очищаем поле ввода задержки"):
            delay_input.clear()
        with allure.step("Вводим значение задержки 45"):
            delay_input.send_keys(delay)

    @allure.step("Нажать кнопки с значениями 7,+,8,=.")
    def press_buttons(self):
        """
        Нажимает на несколько кнопок калькулятора по очереди.
        """
        self.driver.find_element(By.XPATH, "//*[text()='7']").click()
        self.driver.find_element(By.XPATH, "//*[text()='+']").click()
        self.driver.find_element(By.XPATH, "//*[text()='8']").click()
        self.driver.find_element(By.XPATH, "//*[text()='=']").click()

    @allure.step("Функция возвращает конечный результат")
    def return_result(self):
        """
        Возвращает текущий результат с экрана калькулятора.
        """
        with allure.step("Ожидаем получение результата 15 через установленную задержку 45 секунд"):
            self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"div.screen"),"15"))
            result_text = self.driver.find_element(By.CSS_SELECTOR, "div.screen").text
        with allure.step("Получаем результат операции равный 15"):
            return result_text
