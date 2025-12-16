from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("http://uitestingplayground.com/textinput")

input_newButton = browser.find_element(By.CSS_SELECTOR, "#newButtonName")
input_newButton.send_keys("SkyPro")
browser.find_element(By.CSS_SELECTOR,"#updatingButton").click()
new_button = browser.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(new_button)

