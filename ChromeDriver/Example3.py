from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
sleep(5)

# Найти строку поиска и ввести "Selenium"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")

# Нажать Enter для выполнения поиска
search_box.send_keys(Keys.ENTER)
sleep(5)