import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Pages.login_page import LoginPage
from Pages.lost_password_page import RetrievePassword

class TestRetrievePassword(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_retrieve_password(self):
        browser = self.browser

        browser.get("http://demostore.supersqa.com/my-account/")

        # Click forgot password link
        login = LoginPage(browser)
        login.click_forgot_password()

        # Enter email address and click "Reset Password"
        retrieve = RetrievePassword(browser)
        retrieve.enter_username("shopper@gmail.com")
        retrieve.click_reset_password()

        # Verification reset email sent
        confirmation_message = retrieve.get_confirmation_message()
        expected_message = ("Password reset email has been sent.")

        self.assertEqual(confirmation_message, expected_message)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print('Test completed')


