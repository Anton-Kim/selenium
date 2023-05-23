from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    PRODUCT_LINK = (By.CLASS_NAME, 'btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')


class BasketPageLocators:
    PRODUCT_IN_BASKET = (By.CLASS_NAME, 'basket-items')
    EMPTY_BASKET_MESSAGE = (By.XPATH, '//p[contains(text(), "Your basket is empty")]')
