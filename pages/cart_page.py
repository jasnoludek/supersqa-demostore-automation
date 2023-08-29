from locators.locators import Locators
from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, browser):
        self.browser = browser

        self.remove_item_x_css = Locators.remove_item_x_css
        self.product_icon_css = Locators.product_icon_css
        self.product_unit_price_css = Locators.product_unit_price_css
        self.item_quantity_input_css = Locators.item_quantity_input_css
        self.items_subtotal_css = Locators.items_subtotal_css
        self.cart_subtotal_css = Locators.cart_subtotal_css
        self.cart_total_css = Locators.cart_total_css
        self.proceed_to_checkout_button_css = Locators.proceed_to_checkout_button_css

    def get_product_icon(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.product_icon_css)

    def get_product_unit_price(self):
        return self.browser.find_elements(By.CSS_SELECTOR, self.product_unit_price_css)

    def get_item_quantity_input(self):
        return self.browser.find_elements(By.CSS_SELECTOR, self.item_quantity_input_css)

    def get_items_subtotal(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.items_subtotal_css)

    def get_cart_subtotal(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.cart_subtotal_css)

    def get_cart_total(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.cart_total_css)

    def proceed_to_checkout(self):
        self.browser.find_element(By.CSS_SELECTOR, self.proceed_to_checkout_button_css).click()