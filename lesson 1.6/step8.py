from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_xpath_form"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.TAG_NAME, 'input')
input1.send_keys("Damir")
input2 = browser.find_element(By.NAME, 'last_name')
input2.send_keys("Damirgigos")
input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
input3.send_keys("Msk")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("Russia")
button = browser.find_element(By.XPATH, "//button[@type='submit']")

button.click()


time.sleep(5)
browser.quit()