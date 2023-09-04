from locators.locators import Locators
from selenium.webdriver.common.by import By

class MyAccountPage():

    def __init__(self, browser):
        self.browser = browser

        self.logout_button_css = Locators.logout_button_css
        self.home_page_tab_css = Locators.home_page_tab_css

    # Buttons
    def click_logout(self):
        self.browser.find_element(By.CSS_SELECTOR, self.logout_button_css).click()

    def click_home(self):
        self.browser.find_element(By.CSS_SELECTOR, self.home_page_tab_css).click()




