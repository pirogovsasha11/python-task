import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    edge_service = EdgeService(r"C:\Users\Alex\Desktop\edgedriver_win64\msedgedriver.exe")
    driver = webdriver.Edge(service=edge_service)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()
    yield driver
    driver.quit()

#Делаю функцию для повторяющейся операции

def fill_form(driver):

    fields = {
        'input[name="first-name"]': "Иван",
        'input[name="last-name"]': "Петров",
        'input[name="address"]': "Ленина, 55-3",
        'input[name="e-mail"]': "test@skypro.com",
        'input[name="phone"]': "+7985899998787",
        'input[name="city"]': "Москва",
        'input[name="country"]': "Россия",
        'input[name="job-position"]': "QA",
        'input[name="company"]': "SkyPro",
    }

    for selector, value in fields.items():
        driver.find_element(By.CSS_SELECTOR, selector).send_keys(value)


    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3").click()

def wait_for_class(driver, selector, expected_class, timeout=10):
    waiter = WebDriverWait(driver, timeout)
    element = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    waiter.until(lambda d: element.get_attribute("class") == expected_class)
    return element

# 1. Тест: Заполняю и отправляю форму
def test_fill_and_submit_form(driver):
    fill_form(driver)

# 2. Тест: Проверяю (assert), что поле Zip code подсвечено красным.
def test_zip_code_highlight_red(driver):
    fill_form(driver)
    zip_code_element = wait_for_class(driver, '#zip-code', 'alert py-2 alert-danger')
    assert "alert-danger" in zip_code_element.get_attribute("class")

# 3. Тест: Проверяю (assert), что остальные поля подсвечены зеленым.
def test_other_fields_highlight_green(driver):
    fill_form(driver)
    green_class = "alert py-2 alert-success"
    fields_selectors = [
        "#first-name", "#last-name", "#address", "#city",
        "#country", "#e-mail", "#phone", "#job-position", "#company"
    ]
    for selector in fields_selectors:
        element = wait_for_class(driver, selector, green_class)
        assert green_class in element.get_attribute("class")