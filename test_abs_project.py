import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# class TestAbs(unittest.TestCase):
#     def test_reg1(self):
#         browser = webdriver.Chrome()
#         browser.get('http://suninjuly.github.io/registration1.html')
#
#         input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
#         input1.send_keys('Ivan')
#         input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
#         input2.send_keys('Petrov')
#         input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
#         input3.send_keys('ivan@mail.ru')
#
#         button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
#         button.click()
#
#         time.sleep(1)
#
#         welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#         welcome_text = welcome_text_elt.text
#
#         self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be absolute value of a number")
#
#         time.sleep(3)
#         browser.quit()
#
#     def test_reg2(self):
#         browser = webdriver.Chrome()
#         browser.get('http://suninjuly.github.io/registration2.html')
#
#         input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
#         input1.send_keys('Ivan')
#         input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
#         input2.send_keys('Petrov')
#         input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
#         input3.send_keys('ivan@mail.ru')
#
#         button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
#         button.click()
#
#         time.sleep(1)
#
#         welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#         welcome_text = welcome_text_elt.text
#
#         self.assertEqual("Congratulations! You have successfully registered!",
#                          welcome_text, "Should be absolute value of a number")
#
#         time.sleep(3)
#         browser.quit()


if __name__ == "__main__":
    unittest.main()
