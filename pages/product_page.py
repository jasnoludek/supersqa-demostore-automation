from locators.locators import Locators
from selenium.webdriver.common.by import By

class ProductPage():

    def __init__(self, browser):
        self.browser = browser

        self.add_to_cart_button_css = Locators.add_to_cart_button_css
        self.added_to_cart_confirmation_message_css = Locators.added_to_cart_confirmation_message_css
        self.view_cart_button_css = Locators.view_cart_button_css
        self.quantity_input_css = Locators.quantity_input_css

    def add_item_to_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, self.add_to_cart_button_css).click()

    def get_confirmation_message(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.added_to_cart_confirmation_message_css).text

    def click_view_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, self.view_cart_button_css).click()

    def set_quantity(self, quantity):
        quantity_input = self.browser.find_element(By.CSS_SELECTOR, self.quantity_input_css)
        quantity_input.clear()
        quantity_input.send_keys(str(quantity))






