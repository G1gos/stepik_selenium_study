from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/get_attribute.html'
try:
    browser.get(link)

    x_element = browser.find_element(By.ID, 'treasure')
    x_value = x_element.get_attribute('valuex')
    y = calc(str(x_value))

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()
    robot_button = browser.find_element(By.ID, 'robotsRule')
    robot_button.click()

    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit.click()

finally:
    time.sleep(50)
    browser.quit()
