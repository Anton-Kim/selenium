import pytest
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage

# link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
tested_links = [f'{link}?promo=offer{i}' if i != 7 else
                pytest.param(f"{link}?promo=offer{i}",
                             marks=pytest.mark.xfail(reason="some bug", strict=True)
                             )
                for i in range(10)]


# @pytest.mark.parametrize('url', tested_links)
# def test_guest_can_add_product_to_basket(browser, url):
#     page = ProductPage(browser, url)
#     page.open()
#     page.add_to_cart()
#     page.solve_quiz_and_get_code()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_be_disappeared()
