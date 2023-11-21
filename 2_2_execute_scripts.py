from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"

try:
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    result = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(result)
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(5)
    browser.quit()

