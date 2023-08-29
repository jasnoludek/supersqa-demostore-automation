from locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage:

    def __init__(self, browser):
        self.browser = browser

        self.search_field_css = Locators.search_field_css

        self.myAccount_link_css = Locators.myAccount_link_css

        self.first_product_title_css = Locators.first_product_title_css

        self.third_product_add_to_cart_button_css = Locators.third_product_add_to_cart_button_css
        self.album_listed_price_css = Locators.album_listed_price_css

        self.cart_total_amount_css = Locators.cart_total_amount_css

        self.product_page_forward_arrow_css = Locators.product_page_forward_arrow_css
        self.product_page_back_arrow_css = Locators.product_page_back_arrow_css
        self.product_results_indicator_css = Locators.product_results_indicator_css

        self.product_page_one_button_css = Locators.product_page_one_button_css
        self.product_page_two_button_css = Locators.product_page_two_button_css
        self.product_page_three_button_css = Locators.product_page_three_button_css

        self.album_css = Locators.album_css

    def click_myAccount(self):
        self.browser.find_element(By.CSS_SELECTOR, self.myAccount_link_css).click()

    def get_items_count(self):
        product_items = self.browser.find_elements(By.CSS_SELECTOR, Locators.product_list_css)
        return len(product_items)

    def get_product_title(self):
        product_title = self.browser.find_element(By.CSS_SELECTOR, Locators.first_product_title_css)
        return product_title.text

    def click_add_album_to_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, self.third_product_add_to_cart_button_css).click()

    # Product page arrow buttons
    def click_product_page_forward_arrow(self):
        self.browser.find_element(By.CSS_SELECTOR, self.product_page_forward_arrow_css).click()

    def click_product_page_back_arrow(self):
        self.browser.find_element(By.CSS_SELECTOR, self.product_page_back_arrow_css).click()

    # Product page number buttons
    def click_product_page_one_button(self):
        self.browser.find_element(By.CSS_SELECTOR, self.product_page_one_button_css).click()

    def click_product_page_two_button(self):
        self.browser.find_element(By.CSS_SELECTOR, self.product_page_two_button_css).click()

    def click_product_page_three_button(self):
        self.browser.find_element(By.CSS_SELECTOR, self.product_page_three_button_css).click()

    # Product numbers page display
    def get_product_results_text(self):
        product_results_element = self.browser.find_element(By.CSS_SELECTOR, self.product_results_indicator_css)
        return product_results_element.text

    # Click on album product
    def click_album(self):
        self.browser.find_element(By.CSS_SELECTOR, self.album_css).click()

    def get_item_price(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.album_listed_price_css).text

    def get_cart_total(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.cart_total_amount_css).text

    def search(self, product):
        self.browser.find_element(By.CSS_SELECTOR, self.search_field_css).clear()
        self.browser.find_element(By.CSS_SELECTOR, self.search_field_css).send_keys(product)
        self.browser.find_element(By.CSS_SELECTOR, self.search_field_css).send_keys(Keys.RETURN)
