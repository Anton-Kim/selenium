import time
import math
import pytest
from selenium.webdriver.common.by import By

# 8 задач


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'])
class TestStepik:
    def test_stepik_login(self, browser, link):
        browser.get(link)

        browser.find_element(By.ID, 'ember33').click()
        browser.find_element(By.ID, 'id_login_email').send_keys('obsos32@gmail.com')
        browser.find_element(By.ID, 'id_login_password').send_keys('Qwedcxzas88')
        browser.find_element(By.CSS_SELECTOR, '[class="sign-form__btn button_with-loader "]').click()

        answer = math.log(int(time.time()))
        print(answer)
        time.sleep(2.5)
        browser.find_element(By.CSS_SELECTOR, 'textarea').send_keys(str(answer))
        time.sleep(0.5)
        browser.find_element(By.CLASS_NAME, 'submit-submission').click()

        message = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
        if message != 'Correct!':
            print(message)
