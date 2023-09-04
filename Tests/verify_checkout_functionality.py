import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckOutPage


class TestEndToEndPurchase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_end_to_end_purchase(self):
        browser = self.browser

        browser.get("http://demostore.supersqa.com/")

        homepage = HomePage(browser)
        login = LoginPage(browser)
        myaccount = MyAccountPage(browser)
        product = ProductPage(browser)
        cart_page = CartPage(browser)
        checkout_page = CheckOutPage(browser)

        # Login to account
        homepage.click_myAccount()
        login.enter_username('shopper@gmail.com')
        login.enter_password('MyPassword1234$')
        login.click_login()

        # Navigate back to home page
        myaccount.click_home()

        # Click on product
        homepage.click_album()

        # Add item to cart
        product.add_item_to_cart()

        # Verify item added to cart
        item_added_confirmation_message = product.get_confirmation_message()
        expected_message = 'View cart\n“Album” has been added to your cart.'
        self.assertEqual(item_added_confirmation_message, expected_message)

        # Go to cart by clicking "View Cart"
        product.click_view_cart()

        # Verify product items, unit prices, item quantities
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
            cart_total_amount = float(cart_total_amount_text[1:])  # Removing the dollar sign

            self.assertEqual(total_price, cart_total_amount)

        # Proceed to checkout
        cart_page.proceed_to_checkout()

        # Expected totals
        expected_product_subtotal = "$15.00"
        expected_order_subtotal = "$15.00"
        expected_order_total = "$15.00"

        # Get the displayed totals
        actual_product_subtotal = checkout_page.get_product_subtotal().text
        actual_order_subtotal = checkout_page.get_order_subtotal().text
        actual_order_total = checkout_page.get_order_total().text

        # Compare expected and displayed totals
        self.assertEqual(actual_product_subtotal, expected_product_subtotal,
                         f"Product Subtotal: {actual_product_subtotal} != {expected_product_subtotal}")
        self.assertEqual(actual_order_subtotal, expected_order_subtotal,
                         f"Order Subtotal: {actual_order_subtotal} != {expected_order_subtotal}")
        self.assertEqual(actual_order_total, expected_order_total,
                         f"Product Subtotal: {actual_order_total} != {expected_order_total}")

        # Enter coupon code
        checkout_page.click_coupon_link()

        # Wait for the coupon code input to be visible and then enter the code
        coupon_input_locator = checkout_page.coupon_code_textbox_id
        coupon_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.ID, coupon_input_locator))
        )
        coupon_input.clear()
        coupon_input.send_keys("SSQA100")
        checkout_page.click_apply_coupon_button()

        # Wait for the coupon discount amount to be present and visible
        coupon_discount_locator = checkout_page.coupon_discount_amount_css
        coupon_discount_element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, coupon_discount_locator))
        )

        # Get the coupon discount amount
        discount_amount = coupon_discount_element.text

        # Verify coupon applied to total
        expected_discount_amount = "$15.00"
        self.assertEqual(expected_discount_amount, discount_amount)

        # Verify new total = $0.00
        expected_new_total = "$0.00"
        new_total_locator = checkout_page.order_total_css
        new_total_element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, new_total_locator))
        )
        new_total = new_total_element.text
        self.assertEqual(expected_new_total, new_total)

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

        # Click "Place order"
        checkout_page.click_place_order()

        # Verification of order placement
        expected_verification_message = "Thank you. Your order has been received."

        # Wait for the order confirmation message to be visible
        verification_message_locator = checkout_page.order_received_confirmation_xpath
        verification_message_element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, verification_message_locator))
        )
        actual_verification_message = verification_message_element.text
        self.assertEqual(expected_verification_message, actual_verification_message)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print('Test completed')
