import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.cart_page import CartPage


class TestRemoveOneCartItem(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # Initialize the Chrome WebDriver
        cls.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_remove_from_cart(self):
        browser = self.browser
        self.browser.implicitly_wait(5)

        # Open the website
        browser.get("http://demostore.supersqa.com/")

        homepage = HomePage(browser)
        cartpage = CartPage(browser)

        # Search for a product
        homepage.search("beanie")

        results = homepage.get_hoodie_search_results()
        count = len(results)
        assert count == 2  # Verify there are 2 search results

        # Add the found products to the cart
        for result in results:
            add_to_cart_buttons = homepage.get_add_to_cart_buttons()
            for button in add_to_cart_buttons:
                button.click()

        # Go to the cart
        homepage.click_cart()

        wait = WebDriverWait(self.browser, 10)
        cart_items = wait.until(EC.presence_of_all_elements_located((By.XPATH, cartpage.cart_item_row_xpath)))
        count = len(cart_items)
        assert count == 2  # Verify there are 2 items in the cart

        # Calculate the sum of the product prices
        prices = cartpage.get_product_subtotals()
        subtotal_sum = 0
        for price in prices:
            price_value = float(price.text[1:])
            subtotal_sum += price_value

        print("Calculated sum:", subtotal_sum)

        # Get the subtotal value
        subtotal_text = cartpage.get_subtotal().text
        subtotal_value = float(subtotal_text[1:])  # Remove dollar sign and convert to float
        assert subtotal_sum == subtotal_value  # Verify the calculated sum matches the subtotal

        print("Subtotal:", subtotal_value)

        print("Original list of items in cart:")
        for cart_item in cart_items:
            print(cart_item.text)

        # Remove an item from the cart
        remove_item_buttons = cartpage.get_remove_from_cart_buttons()
        remove_item_buttons[1].click()

        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.staleness_of(cart_items[1]))

        # Verify only one item left in cart
        remaining_item = wait.until(EC.presence_of_element_located((By.XPATH, cartpage.cart_item_row_xpath)))
        assert remaining_item is not None
        print("Only one item remaining:", remaining_item.text)

        # Calculate the sum of remaining items' prices
        remaining_prices = cartpage.get_product_subtotals()
        remaining_sum = sum([float(price.text[1:]) for price in remaining_prices])

        # Get the updated subtotal after item removal
        updated_subtotal_text = cartpage.get_subtotal().text
        updated_subtotal_value = float(updated_subtotal_text[1:])

        # Assert that the calculated sum matches the updated subtotal
        assert remaining_sum == updated_subtotal_value
        print("Calculated sum of remaining items:", remaining_sum)
        print("Updated subtotal after removal:", updated_subtotal_value)

    @classmethod
    def tearDown(cls):
        cls.browser.close()
        cls.browser.quit()
        print('Test Completed')

