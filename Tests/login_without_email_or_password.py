import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Pages.home_page import HomePage
from Pages.login_page import LoginPage

class loginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_login_without_email_or_password(self):
        browser = self.browser

        browser.get("http://demostore.supersqa.com/")

        homepage = HomePage(browser)
        homepage.click_myAccount()

        login = LoginPage(browser)
        login.click_login()

        time.sleep(2)

        # Verification of unsuccessful login
        error_message = login.get_no_username_error_message()
        expected_error_message = ("Error: Username is required.")

        self.assertEqual(error_message, expected_error_message)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print('Test completed')

