import time
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(n):
  return str(math.log(abs(12*math.sin(int(n)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'
try:
    browser = webdriver.Chrome()
    # browser.implicitly_wait(5)
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    browser.find_element(By.ID, 'book').click()

    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.ID, 'solve').click()


    # browser.find_element(By.CSS_SELECTOR, '.trollface').click()
    # browser.switch_to.window(browser.window_handles[1])

    # browser.switch_to.alert.accept()

    # browser.find_element(By.NAME, 'firstname').send_keys('Ivan')
    # browser.find_element(By.NAME, 'lastname').send_keys('Petrov')
    # browser.find_element(By.NAME, 'email').send_keys('iv@mail.ru')

    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_path = os.path.join(current_dir, 'file.txt')
    # browser.find_element(By.ID, 'file').send_keys(file_path)

    # input1 = browser.find_element(By.ID, 'answer')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    # input1.send_keys(calc(x))

    # s = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    # s.select_by_visible_text(str(int(n1) + int(n2)))

    # browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    # browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()

    # elements = browser.find_elements(By.TAG_NAME, 'input')
    # for element in elements:
    #     element.send_keys("I")

    # browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(5)
    browser.quit()
