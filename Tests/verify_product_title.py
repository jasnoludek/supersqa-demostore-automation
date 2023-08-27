import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage

class TestProductTitle(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_product_title(self):
        browser = self.browser

        browser.get("http://demostore.supersqa.com/")

        homepage = HomePage(browser)

        actual_product_title = homepage.get_product_title()
        expected_product_title = "Jeans"

        self.assertEqual(actual_product_title, expected_product_title)

        print(f'Expected Product Title: {expected_product_title}')
        print(f'Actual Product Title: {actual_product_title}')

    @classmethod
    def tearDown(cls):
        cls.browser.close()
        cls.browser.quit()
        print('Test Completed')



