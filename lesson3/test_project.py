from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = 'http://suninjuly.github.io/registration2.html'


def test_link_1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    first_name.send_keys("Nik")
    last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    last_name.send_keys("Krispin")
    email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    email.send_keys("nik@mail.com")
    time.sleep(1)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert ("Congratulations! You have successfully registered!", welcome_text, f"You didn't got "
                                                                                f"Congratulations")


def test_link_2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    first_name.send_keys("Nik")
    last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    last_name.send_keys("Krispin")
    email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    email.send_keys("nik@mail.com")
    time.sleep(1)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert ("Congratulations! You have successfully registered!", welcome_text, f"You didn't got "
                                                                                f"Congratulations")


if __name__ == "main":
    test_link_1()
    test_link_2()
