import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from Pages.my_account_page import MyAccountPage

class loginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_login_and_logout(self):
        browser = self.browser

        browser.get("http://demostore.supersqa.com/")

        homepage = HomePage(browser)
        homepage.click_myAccount()

        login = LoginPage(browser)
        login.enter_username('shopper@gmail.com')
        login.enter_password('MyPassword1234$')
        login.click_login()

        time.sleep(2)

        # Verification of login
        hello_message = self.browser.find_element(By.XPATH, '//*[@id="post-9"]/div/div/div/p[1]')
        user = self.browser.find_element(By.XPATH, '//*[@id="post-9"]/div/div/div/p[1]/strong[1]')
        assert hello_message.is_displayed(), "Hello message is not displayed"
        assert user.text in hello_message.text
        hello_message_text = hello_message.text
        print(f"Confirmation user is logged in: "
              f"{hello_message_text}")

        # Perform logout
        logout = MyAccountPage(browser)
        logout.click_logout()

        # Verification of logout
        email_field = self.browser.find_element(By.ID, login.username_textbox_id)
        password_field = self.browser.find_element(By.ID, login.password_textbox_id)

        assert email_field.is_displayed(), "Email field is not displayed"
        assert password_field.is_displayed(), "Password field is not displayed"

        print("User successfully logged out and login fields are present again")

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print('Test completed')



