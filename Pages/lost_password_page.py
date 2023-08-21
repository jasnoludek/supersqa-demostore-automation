from Locators.locators import Locators
from selenium.webdriver.common.by import By

class RetrievePassword():

    def __init__(self, browser):
        self.browser = browser

        # Input field
        self.username_lost_password_textbox_id = Locators.username_lost_password_textbox_id

        # Reset password button
        self.reset_password_button_css = Locators.reset_password_button_css

        # Confirmation message
        self.reset_email_sent_confirmation_css = Locators.reset_email_sent_confirmation_css

    def enter_username(self, username):
        self.browser.find_element(By.ID, self.username_lost_password_textbox_id).clear()
        self.browser.find_element(By.ID, self.username_lost_password_textbox_id).send_keys(username)

    def click_reset_password(self):
        self.browser.find_element(By.CSS_SELECTOR, self.reset_password_button_css).click()

    def get_confirmation_message(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.reset_email_sent_confirmation_css).text
