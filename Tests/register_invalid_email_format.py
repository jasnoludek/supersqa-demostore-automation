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
        register = RegistrationPage(browser)

        # Navigate to login page
        homepage.click_myAccount()

        # Attempt to register with invalid email address
        register.register_username('bademailgmail.com')
        register.register_password('NewPassword1234!')
        register.click_register()

        time.sleep(2)

        # Verify JavaScript alert
        alert = browser.switch_to.
        alert_text = alert.text
        print(f"Alert message displayed: {alert_text}")
        alert.accept()

        # Verification (intentional failure scenario)
        page_source = browser.page_source
        expected_error_message = "Invalid email format"
        assert expected_error_message in page_source, f"Expected error message '{expected_error_message}' not found on the page"

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print('Test completed')




