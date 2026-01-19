import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from main_page import MainPage
from login_page import LoginPage
from product_page import ProductPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.id("SKYPRO-2")
@allure.story("Проверка функциональности интернет-магазина")
@allure.epic("Интернет-магазин")
@allure.severity("CRITICAL")
@allure.title("Тест оформление заказа в интернет-магазине")
@allure.description("Данный тест включает в себя шаги:"
                    " открыть сайт магазина,"
                    " авторизоваться как пользователь standard_user,"
                    " добавить в корзину товары,"
                    " перейти в корзину,"
                    " нажать кнопку Checkout,"
                    " заполнить форму своими данными,"
                    " прочитать со страницы итоговую стоимость,"
                    " закрыть браузер,"
                    " проверить, что итоговая сумма равна $58.29")
def test_full_purchase_flow():
    """
    Тестовый сценарий покупки нескольких товаров в интернет-магазине одежды
    """
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    main = MainPage(driver)
    login = LoginPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    main.open()
    login.username("standard_user")
    login.password("secret_sauce")
    login.click_button()

    product.add_product_cart("Sauce Labs Backpack")
    product.add_product_cart("Sauce Labs Bolt T-Shirt")
    product.add_product_cart("Sauce Labs Onesie")
    product.go_cart()

    cart.checkout()

    checkout.first_name("Alex")
    checkout.last_name("Grant")
    checkout.postal_code("142625")
    checkout.click_continue()

    total = checkout.check_total_price()
    with allure.step("Проверить что итоговая сумма равна $58.29"):
        assert total == "Total: $58.29"

    driver.quit()