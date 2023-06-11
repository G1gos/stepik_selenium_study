import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)
    # button = WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.ID, "verify")))
    button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 25).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button.click()

    num = browser.find_element(By.ID, 'input_value').text
    final = calc(num)
    answer_view = browser.find_element(By.ID, 'answer')
    answer_view.send_keys(str(final))
    browser.find_element(By.ID, 'solve').click()

finally:
    time.sleep(5)
    browser.quit()