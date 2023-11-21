from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = calc(x)
    time.sleep(1)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(result)
    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    print(result)

finally:
    time.sleep(5)
    browser.quit()

