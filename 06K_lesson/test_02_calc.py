import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()
    yield driver
    driver.quit()

# Тест: Проверяю (assert), что в окне отобразится результат 15 через 45 секунд.
def test_calculator(driver):
    waiter = WebDriverWait(driver, 50)
    delay_input = driver.find_element(By.CSS_SELECTOR, '#delay')
    delay_input.clear()
    delay_input.send_keys('45')

    driver.find_element(By.XPATH, "//*[text()='7']").click()
    driver.find_element(By.XPATH, "//*[text()='+']").click()
    driver.find_element(By.XPATH, "//*[text()='8']").click()
    driver.find_element(By.XPATH, "//*[text()='=']").click()

    waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"div.screen"),"15"))
    result_text = driver.find_element(By.CSS_SELECTOR, "div.screen").text
    assert result_text == "15"