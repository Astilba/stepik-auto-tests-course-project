from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Product is in a basket, but should not be"

    def should_be_empty_basket_massage(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), 'No empty basket message'
