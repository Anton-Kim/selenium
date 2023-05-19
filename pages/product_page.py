from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        product_link = self.browser.find_element(*ProductPageLocators.PRODUCT_LINK)
        product_link.click()
