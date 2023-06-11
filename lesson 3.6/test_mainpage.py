import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math




@pytest.fixture()
def browser():
    print("\nstart browser for test suite..")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    browser = webdriver.Chrome(chrome_options=chrome_options)
    yield browser
    # выполняется тест, который вызвал фикстуру
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"
                                  ])
class TestMainpage:
    def test_main(self, browser, link):

        browser.get(f"{link}")
        income = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "ember33")))
        income.click()

        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'id_login_email')))
        browser.find_element(By.ID, 'id_login_email').send_keys("gimranov500@gmail.com")
        browser.find_element(By.ID, "id_login_password").send_keys("Rezyrjdj1999123")

        time.sleep(3)
        income2 = browser.find_element(By.CSS_SELECTOR, "button.button_with-loader ")
        income2.click()
        time.sleep(5)

        answer = math.log(int(time.time()))
        browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea").send_keys(
            str(answer))
        time.sleep(3)
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        time.sleep(3)
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME,
                                                                                    "smart-hints__hint")))
        is_right_answer = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
        print(is_right_answer)
        assert "Correct!" == is_right_answer
