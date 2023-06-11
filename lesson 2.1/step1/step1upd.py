import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

link = 'https://suninjuly.github.io/selects1.html'

try:
    browser.get(link)
    num1 = browser.find_element(By.ID, 'num1')
    new_num1 = int(num1.text)
    num1 = browser.find_element(By.ID, 'num2')
    new_num2 = int(num1.text)
    summ = new_num1 + new_num2
    str_summ = str(summ)
    browser.find_element(By.ID, 'dropdown').click()
    browser.find_element(By.CSS_SELECTOR, f'[value="{str_summ}"]').click()

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(5)
    browser.quit()