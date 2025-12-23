from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_cart(self, item_name):
        self.driver.find_element(By.XPATH, f"//div[text()='{item_name}']/../../..//button").click()

    def go_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container').click()