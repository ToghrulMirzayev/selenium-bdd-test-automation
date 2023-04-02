from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    TITLE_TEXT = (By.CSS_SELECTOR, ".title")
    CART_ICON = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def add_product_to_cart(self):
        self.wait_for_element(self.ADD_TO_CART_BUTTON).click()

    def is_title_text_displayed(self):
        return self.wait_for_element(self.TITLE_TEXT).is_displayed()

    def is_product_in_cart(self):
        return self.wait_for_element(self.CART_ICON).is_displayed()
