
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/login")

search_input_username = driver.find_element(By.CSS_SELECTOR, "#username")
search_input_username.send_keys("tomsmith")
sleep(2)
search_input_password = driver.find_element(By.CSS_SELECTOR, "#password")
search_input_password.send_keys("SuperSecretPassword!")
sleep(2)
login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()

Secure_Area = driver.find_element(By.CSS_SELECTOR, "#flash").text
print(Secure_Area)

driver.quit()
