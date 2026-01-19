import allure
import pytest
from selenium import webdriver
from Calculator import Calculator


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации драйвера Chrome
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.id("SKYPRO-1")
@allure.story("Проверка функциональности Калькулятора")
@allure.feature("Калькулятор")
@allure.title("Сложение в калькуляторе")
@allure.severity("BLOCKER")
@allure.description("Тест проверяет, что результат калькулятора равен 15"
                    " после ввода указанных в условиях значений и задержки 45 секунд.")
def test_calculator(driver):
    """
    Тест проверяет, что результат калькулятора равен 15
    """
    calc_page = Calculator(driver)
    calc_page.open()
    calc_page.set_delay(45)
    calc_page.press_buttons()
    assert calc_page.return_result() == '15'
