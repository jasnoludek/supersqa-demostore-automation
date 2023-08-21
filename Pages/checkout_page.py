from Locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class CheckOutPage:

    def __init__(self, browser):
        self.browser = browser

        # Order total verification
        self.product_subtotal_css = Locators.product_subtotal_css
        self.order_subtotal_css = Locators.order_subtotal_css
        self.order_total_css = Locators.order_total_css

        # Coupon code link, input and button
        self.coupon_code_link_css = Locators.coupon_code_link_css
        self.coupon_code_textbox_id = Locators.coupon_code_textbox_id
        self.apply_coupon_button_css = Locators.apply_coupon_button_css

        self.coupon_discount_amount_css = Locators.coupon_discount_amount_css

        # Billing details
        self.billing_firstname_textbox_id = Locators.billing_firstname_textbox_id
        self.billing_lastname_textbox_id = Locators.billing_lastname_textbox_id
        self.billing_company_name_textbox_id = Locators.billing_company_name_textbox_id
        self.billing_country_selector_id = Locators.billing_country_selector_id
        self.billing_street_address_textbox_id = Locators.billing_street_address_textbox_id
        self.billing_apartment_textbox_id = Locators.billing_apartment_textbox_id
        self.billing_city_textbox_id = Locators.billing_city_textbox_id
        self.billing_state_dropdownbox_id = Locators.billing_state_dropdownbox_id
        self.billing_postcode_textbox_id = Locators.billing_postcode_textbox_id
        self.billing_phone_number_textbox_id = Locators.billing_phone_number_textbox_id
        self.billing_billing_email_textbox_id = Locators.billing_billing_email_textbox_id
        self.billing_notes_textbox_id = Locators.billing_notes_textbox_id

        # Place order button
        self.place_order_button_id = Locators.place_order_button_id

        # Order received confirmation
        self.order_received_confirmation_css = Locators.order_received_confirmation_css

    def get_product_subtotal(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.product_subtotal_css)

    def get_order_subtotal(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.order_subtotal_css)

    def get_order_total(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.order_total_css)

    def click_coupon_link(self):
        self.browser.find_element(By.CSS_SELECTOR, self.coupon_code_link_css).click()

    def enter_coupon_code(self, coupon_code):
        self.browser.find_element(By.ID, self.coupon_code_textbox_id).clear()
        self.browser.find_element(By.ID, self.coupon_code_textbox_id).send_keys(coupon_code)

    def click_apply_coupon_button(self):
        self.browser.find_element(By.CSS_SELECTOR, self.apply_coupon_button_css).click()

    def get_discount_amount(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.coupon_discount_amount_css)

    def enter_firstname(self, firstname):
        self.browser.find_element(By.ID, self.billing_firstname_textbox_id).clear()
        self.browser.find_element(By.ID, self.billing_firstname_textbox_id).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.browser.find_element(By.ID, self.billing_lastname_textbox_id).clear()
        self.browser.find_element(By.ID, self.billing_lastname_textbox_id).send_keys(lastname)

    def enter_company_name(self, company_name):
        self.browser.find_element(By.ID, self.billing_company_name_textbox_id).clear()
        self.browser.find_element(By.ID, self.billing_company_name_textbox_id).send_keys(company_name)

    def enter_street_address(self, street_address):
        self.browser.find_element(By.ID, self.billing_street_address_textbox_id).clear()
        self.browser.find_element(By.ID, self.billing_street_address_textbox_id).send_keys(street_address)

    def enter_apartment(self, apartment):
        self.browser.find_element(By.ID, self.billing_apartment_textbox_id).clear()
        self.browser.find_element(By.ID, self.billing_apartment_textbox_id).send_keys(apartment)

    def enter_city(self, city):
        self.browser.find_element(By.ID, self.billing_city_textbox_id).clear()
        self.browser.find_element(By.ID, self.billing_city_textbox_id).send_keys(city)

    def select_state(self, state):
        find_state = self.browser.find_element(By.ID, self.billing_state_dropdownbox_id)
        select_state = Select(find_state)
        select_state.select_by_visible_text(state)

    def enter_zip_code(self, postcode):
        self.browser.find_element(By.ID, self.billing_postcode_textbox_id).clear()
        self.browser.find_element(By.ID, self.billing_postcode_textbox_id).send_keys(postcode)

    def enter_phone_number(self, phone_number):
        self.browser.find_element(By.ID, self.billing_phone_number_textbox_id).clear()
        self.browser.find_element(By.ID, self.billing_phone_number_textbox_id).send_keys(phone_number)

    def enter_order_notes(self, order_notes):
        self.browser.find_element(By.ID, self.billing_notes_textbox_id).clear()
        self.browser.find_element(By.ID, self.billing_notes_textbox_id).send_keys(order_notes)

    def click_place_order(self):
        self.browser.find_element(By.ID, self.place_order_button_id).click()

    def get_order_confirmation(self):
        return self.browser.find_element(By.XPATH, self.order_received_confirmation_css)

