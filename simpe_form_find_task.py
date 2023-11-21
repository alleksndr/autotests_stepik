from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser.get(link)
    time.sleep(1)

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    time.sleep(1)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла