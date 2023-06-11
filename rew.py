from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    first_name.send_keys("Nik")

    last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    last_name.send_keys("Krupin")

    email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    email.send_keys("nik@mail.com")
    time.sleep(1)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(1)
    browser.quit()