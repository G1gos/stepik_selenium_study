import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()
    confirm = browser.switch_to.alert
    confirm.accept()

    num = browser.find_element(By.ID, 'input_value').text
    final = calc(num)
    answer_view = browser.find_element(By.ID, 'answer')
    answer_view.send_keys(str(final))
    browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()

finally:
    time.sleep(10)
    browser.quit()

