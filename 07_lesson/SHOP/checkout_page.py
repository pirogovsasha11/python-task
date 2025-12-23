from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def first_name(self,value):
        self.driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(value)

    def last_name(self,value):
        self.driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(value)

    def postal_code(self,value):
        self.driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(value)

    def  click_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def check_total_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
