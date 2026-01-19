import allure


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть сайт магазина")
    def open(self):
        """
        Открытие страницы интернет-магазина одежды
        """
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()