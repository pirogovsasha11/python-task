import pytest
from selenium import webdriver
from calc_page import Calculator


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Тест: Проверяю (assert), что в окне отобразится результат 15 через 45 секунд.
def test_calculator(driver):
   calc_page = Calculator(driver)
   calc_page.open()
   calc_page.set_delay(45)
   calc_page.press_buttons()
   assert calc_page.return_result() == '15'
