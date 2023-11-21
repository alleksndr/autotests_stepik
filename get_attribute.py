from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser.get(link)
    time.sleep(1)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(image_attr)))))

    image = browser.find_element(By.ID, "treasure")
    image_attr = image.get_attribute("valuex")
    print(image_attr)

    result = calc(image_attr)
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

