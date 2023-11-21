from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

browser = webdriver.Chrome()
browser.implicitly_wait(15)

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price_exp = WebDriverWait(browser, 15)
    status = price_exp.until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    print(status)

    button = browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    result = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(result)

    button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(1)
    button.click()

finally:
    time.sleep(5)
    browser.quit()
