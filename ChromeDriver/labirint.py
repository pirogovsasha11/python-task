from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# размер страницы сайта
driver.maximize_window()

# зайти на сайт лабиринт
driver.get("https://www.labirint.ru")

# найти книгу в поиске Python и нажать кнопку Поиск
search_input = driver.find_element(By.CSS_SELECTOR, "#search-field")
search_input.send_keys("Python",Keys.ENTER)

sleep(5)  # Добавляем задержку

# собрать все карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")
print(len(books))

# вывести в консоль инфо:название, автор, цена
# text = driver.find_element(By.TAG_NAME, "h1").text
for book in books:
    price = book.find_element(By.CSS_SELECTOR, "div.product-card__price-current").text
    title = book.find_element(By.CSS_SELECTOR, "a.product-card__name").text
    author = ''
    try:
        author = book.find_element(By.CSS_SELECTOR, "div.product-card__author").text
    except:
        author = "Автор не найден"

    print(author + "\t" + title + "\t" + price)

sleep(10)




