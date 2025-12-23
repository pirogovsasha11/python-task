
class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

