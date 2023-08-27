import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage

class TestSingleItemPriceCalculation(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_single_item_price_calculation(self):
        browser = self.browser

        browser.get("http://demostore.supersqa.com/")

        homepage = HomePage(browser)
        homepage.click_add_album_to_cart()

        time.sleep(5)

        # Verification of correct price
        product_item_price_element = homepage.get_item_price()
        cart_total_amount_element = homepage.get_cart_total()
        self.assertEqual(product_item_price_element, cart_total_amount_element)



    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print('Test completed')
