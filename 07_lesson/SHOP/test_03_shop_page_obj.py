from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


from main_page import MainPage
from login_page import LoginPage
from product_page import ProductPage
from cart_page import CartPage
from checkout_page import CheckoutPage



def test_full_purchase_flow():
    # driver = webdriver.Firefox()
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

    assert total == "Total: $58.29"

    driver.quit()
