import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.registration_page import RegistrationPage

class TestInvalidEmailFormat(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_register_invalid_email(self):
        browser = self.browser

        browser.get("http://demostore.supersqa.com/")

        homepage = HomePage(browser)
        homepage.click_myAccount()

        register = RegistrationPage(browser)
        register.register_username('bademailgmail.com')
        register.register_password('NewPassword1234!')
        register.click_register()

        time.sleep(2)

        # Verification (intentional failure scenario)
        page_source = browser.page_source
        expected_error_message = "Invalid email format"
        assert expected_error_message in page_source, f"Expected error message '{expected_error_message}' not found on the page"

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print('Test completed')




