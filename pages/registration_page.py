from locators.locators import Locators
from selenium.webdriver.common.by import By

class RegistrationPage():

    def __init__(self, browser):
        self.browser = browser

        # Input fields
        self.username_reg_textbox_id = Locators.username_reg_textbox_id
        self.password_reg_textbox_id = Locators.password_reg_textbox_id

        # Register button
        self.register_button_css = Locators.register_button_css

    def register_username(self, random_email):
        self.browser.find_element(By.ID, self.username_reg_textbox_id).clear()
        self.browser.find_element(By.ID, self.username_reg_textbox_id).send_keys(random_email)

    def register_password(self, reg_password):
        self.browser.find_element(By.ID, self.password_reg_textbox_id).clear()
        self.browser.find_element(By.ID, self.password_reg_textbox_id).send_keys(reg_password)

    def click_register(self):
        self.browser.find_element(By.CSS_SELECTOR, self.register_button_css).click()