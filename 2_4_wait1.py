from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 3 секунд
browser.implicitly_wait(3)

browser.get("http://suninjuly.github.io/cats.html")

button = browser.find_element(By.ID, "button")