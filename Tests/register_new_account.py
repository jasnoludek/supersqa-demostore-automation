import time
import random
import string
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.registration_page import RegistrationPage

class TestRegisterNewAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_register_new_account(self):
        browser = self.browser

        browser.get("http://demostore.supersqa.com/")

        homepage = HomePage(browser)
        homepage.click_myAccount()

        register = RegistrationPage(browser)
        # Generate random email address
        random_email = self.generate_random_email()
        time.sleep(2)
        # Enter random email address and password
        register.register_username(random_email)
        register.register_password('NewPassword1234!')
        register.click_register()

        # Verification
        page_source = browser.page_source
        random_string = random_email.split('@')[0]
        assert random_string in page_source, f"User name '{random_string}' is not displayed on the page"

        # Print random email address generated and used for account creation
        print(f"Random email: {random_email}")

    @staticmethod
    def generate_random_email():
        random_string = ''.join(random.choices(string.ascii_lowercase, k=8))
        email = f'{random_string}@xmail.com'
        return email

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print('Test completed')

