import time
import unittest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.login_page import LoginPage

class loginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_login_wrong_password(self):
        browser = self.browser

        browser.get("http://demostore.supersqa.com/")

        homepage = HomePage(browser)
        homepage.click_myAccount()

        login = LoginPage(browser)
        login.enter_username('shopper@gmail.com')
        login.enter_password('WrongPassword1234$')
        login.click_login()

        time.sleep(2)

        # Verification of unsuccessful login
        error_message = login.get_wrong_password_error_message()
        expected_error_message = 'Error: The password you entered for the email address shopper@gmail.com is incorrect. Lost your password?'

        self.assertEqual(error_message, expected_error_message)


    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print('Test completed')