from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

waiter = WebDriverWait(browser, 15)

browser.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#landscape")))
award = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#award")))
src_value = award.get_attribute("src")
print(src_value)

browser.quit()
