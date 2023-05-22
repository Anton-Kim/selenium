from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        product_link = self.browser.find_element(*ProductPageLocators.PRODUCT_LINK)
        product_link.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           'Success message is presented, but should not be'

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           'Success message is not disappeared, but should be'
