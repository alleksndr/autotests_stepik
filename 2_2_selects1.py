from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"

try:
    browser.get(link)
    time.sleep(1)

    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    print(num1, num2)

    result = str(int(num1) + int(num2))
    print(result)

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_visible_text(result)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

