import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from Pages.my_account_page import MyAccountPage
from Pages.product_page import ProductPage
from Pages.cart_page import CartPage
from Pages.checkout_page import CheckOutPage


class TestEndToEndPurchase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.checkout_page = CheckOutPage(cls.browser)

    def test_end_to_end_purchase(self):
        browser = self.browser

        browser.get("http://demostore.supersqa.com/")

        # Login to account
        homepage = HomePage(browser)
        homepage.click_myAccount()

        login = LoginPage(browser)
        login.enter_username('shopper@gmail.com')
        login.enter_password('MyPassword1234$')
        login.click_login()

        time.sleep(2)

        # Navigate back to home page
        myaccount = MyAccountPage(browser)
        myaccount.click_home()

        time.sleep(2)

        # Click on product
        homepage = HomePage(browser)
        homepage.click_album()

        time.sleep(2)

        # Add item to cart
        product = ProductPage(browser)
        product.add_item_to_cart()

        # Verify item added to cart
        product = ProductPage(browser)
        item_added_confirmation_message = product.get_confirmation_message()
        expected_message = 'View cart\n“Album” has been added to your cart.'
        self.assertEqual(item_added_confirmation_message, expected_message)

        time.sleep(2)

        # Go to cart by clicking "View Cart"
        product = ProductPage(browser)
        product.click_view_cart()

        time.sleep(2)

        # Verify product items, unit prices, item quantities
        cart_page = CartPage(browser)
        product_unit_price = cart_page.get_product_unit_price()
        item_quantity_input = cart_page.get_item_quantity_input()


        # Define the expected unit price
        expected_unit_price = "$15.00"

        # Iterate through the product unit prices and item quantities
        for price, quantity_input in zip(product_unit_price, item_quantity_input):
            # Retrieve the current quantity
            current_quantity = int(quantity_input.get_attribute('value'))

            # Verify that the unit price matches the expected price
            actual_unit_price = price.text
            self.assertEqual(actual_unit_price, expected_unit_price, f"Expected unit price: {expected_unit_price}, Actual unit price: {actual_unit_price}")

            # Verify that the quantity input contains the correct value (1 in this case)
            actual_quantity = quantity_input.get_attribute('value')
            expected_quantity = "1"
            self.assertEqual(actual_quantity, expected_quantity, f"Expected quantity: {expected_quantity}, Actual quantity: {actual_quantity}")

            # Calculate the total price considering the quantity
            total_price = current_quantity * float(expected_unit_price[1:])  # Removing the dollar sign

            # Verify that the calculated total price matches the displayed total price
            cart_total_amount_element = cart_page.get_cart_total()
            cart_total_amount_text = cart_total_amount_element.text
            cart_total_amount = float(cart_total_amount_text[1:]) # Removing the dollar sign

            self.assertEqual(total_price, cart_total_amount)

        # Proceed to checkout
        cart_page.proceed_to_checkout()

        time.sleep(2)

        # Expected totals
        expected_product_subtotal = "$15.00"
        expected_order_subtotal = "$15.00"
        expected_order_total = "$15.00"

        # Get the displayed totals
        actual_product_subtotal = self.checkout_page.get_product_subtotal().text
        actual_order_subtotal = self.checkout_page.get_order_subtotal().text
        actual_order_total = self.checkout_page.get_order_total().text

        # Compare expected and displayed totals
        self.assertEqual(actual_product_subtotal, expected_product_subtotal,
                         f"Product Subtotal: {actual_product_subtotal} != {expected_product_subtotal}")
        self.assertEqual(actual_order_subtotal, expected_order_subtotal,
                         f"Order Subtotal: {actual_order_subtotal} != {expected_order_subtotal}")
        self.assertEqual(actual_order_total, expected_order_total,
                         f"Product Subtotal: {actual_order_total} != {expected_order_total}")

        # Enter coupon code
        checkout_page = CheckOutPage(browser)
        checkout_page.click_coupon_link()
        time.sleep(2)
        checkout_page.enter_coupon_code("SSQA100")
        checkout_page.click_apply_coupon_button()

        time.sleep(3)

        # Verify coupon applied to total
        expected_discount_amount = "$15.00"
        discount_amount = self.checkout_page.get_discount_amount().text
        self.assertEqual(expected_discount_amount, discount_amount)

        # Verify new total = $0.00
        expected_new_total = "$0.00"
        new_total = self.checkout_page.get_order_total().text
        self.assertEqual(expected_new_total, new_total)

        time.sleep(2)

        # Enter billing data
        checkout_page.enter_firstname('John')
        checkout_page.enter_lastname('Doe')
        checkout_page.enter_company_name('Globochem')
        checkout_page.enter_street_address('123 Main St.')
        checkout_page.enter_apartment('1A')
        checkout_page.enter_city('Anytown')
        checkout_page.select_state("Alabama")
        checkout_page.enter_zip_code('12345')
        checkout_page.enter_phone_number('1231231234')
        checkout_page.enter_order_notes('Thank you.')

        time.sleep(2)

        # Click "Place order"
        checkout_page.click_place_order()

        time.sleep(2)

        # Verification of order placement
        expected_verification_message = "Thank you. Your order has been received."
        actual_verification_message = self.checkout_page.get_order_confirmation().text
        self.assertEqual(expected_verification_message, actual_verification_message)

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print('Test completed')


if __name__ == '__main__':
    unittest.main()










