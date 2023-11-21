from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser.get(link)
    time.sleep(1)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    redirect_btn = browser.find_element(By.CLASS_NAME, "trollface")
    redirect_btn.click()
    time.sleep(1)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(result)
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

