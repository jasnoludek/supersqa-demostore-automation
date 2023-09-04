from locators.locators import Locators
from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, browser):
        self.browser = browser

        # Input fields
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id

        # Login button
        self.login_button_css = Locators.login_button_css

        # Forgot password link
        self.forgot_password_link_css = Locators.forgot_password_link_css

        # Error messages
        self.wrong_password_error_message_css = Locators.wrong_password_error_message_css
        self.no_username_error_message_css = Locators.no_username_error_message_css

    def enter_username(self, username):
        self.browser.find_element(By.ID, self.username_textbox_id).clear()
        self.browser.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.browser.find_element(By.ID, self.password_textbox_id).clear()
        self.browser.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.browser.find_element(By.CSS_SELECTOR, self.login_button_css).click()

    def get_wrong_password_error_message(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.wrong_password_error_message_css).text

    def get_no_username_error_message(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.no_username_error_message_css).text

    def click_forgot_password(self):
        self.browser.find_element(By.CSS_SELECTOR, self.forgot_password_link_css).click()