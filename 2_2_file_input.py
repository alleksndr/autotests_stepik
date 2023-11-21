from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("test@test.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'stepik_file.txt')
    upload = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    upload.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()