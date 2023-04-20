from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# def test_substring(full_string, substring):
#     assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/registration2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    input1.send_keys('Ivan')
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    input2.send_keys('Petrov')
    input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    input3.send_keys('ivan@mail.ru')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    browser.quit()