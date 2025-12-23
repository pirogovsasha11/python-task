from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 46)

    def open(self):
        self.driver.get(
                "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        delay_input.clear()
        delay_input.send_keys(delay)

    def press_buttons(self):
        self.driver.find_element(By.XPATH, "//*[text()='7']").click()
        self.driver.find_element(By.XPATH, "//*[text()='+']").click()
        self.driver.find_element(By.XPATH, "//*[text()='8']").click()
        self.driver.find_element(By.XPATH, "//*[text()='=']").click()

    def return_result(self):
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"div.screen"),"15"))
        result_text = self.driver.find_element(By.CSS_SELECTOR, "div.screen").text
        return result_text
