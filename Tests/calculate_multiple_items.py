import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

class TestMultipleItemsPriceCalculation(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_multiple_items_price_calculation(self):
        browser = self.browser

        browser.get("http://demostore.supersqa.com/")

        # Click on product
        homepage = HomePage(browser)
        homepage.click_album()

        time.sleep(2)

        product_page = ProductPage(self.browser)
        product_page.set_quantity(2)
        product_page.click_add_to_cart()

        time.sleep(2)

        cart_page = CartPage(self.browser)
        product_item_price = cart_page.get_product_item_price()
        cart_total_amount = cart_page.get_cart_total_amount()

        if product_item_price == cart_total_amount:
            print("Prices are equal.")
        else:
            print("Prices are not equal.")

        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print('Test completed')