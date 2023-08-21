import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Pages.home_page import HomePage

class TestHomePageItemCount(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_verify_item_count(self):
        browser = self.browser

        browser.get("http://demostore.supersqa.com/")

        homepage = HomePage(browser)

        actual_item_count = homepage.get_items_count()
        expected_item_count = 16

        self.assertEqual(actual_item_count, expected_item_count)

        print(f'Expected Item Count: {expected_item_count}')
        print(f'Actual Item Count: {actual_item_count}')

    @classmethod
    def tearDown(cls):
        cls.browser.close()
        cls.browser.quit()
        print('Test Completed')



