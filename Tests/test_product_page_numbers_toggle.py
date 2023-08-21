import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Pages.home_page import HomePage

class TestProductPageNumberToggles(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_product_page_number_buttons(self):
        browser = self.browser

        browser.get("http://demostore.supersqa.com/")

        homepage = HomePage(browser)

        # Product results count on page 1
        expected_results_text = "Showing 1–16 of 37 results"
        actual_results_text = homepage.get_product_results_text()
        self.assertEqual(expected_results_text, actual_results_text)

        time.sleep(2)

        # Toggle to results page 2 using "2" button
        homepage.click_product_page_two_button()
        expected_results_text = "Showing 17–32 of 37 results"
        actual_results_text = homepage.get_product_results_text()
        self.assertEqual(expected_results_text, actual_results_text)

        time.sleep(2)

        # Toggle to results page 3 using "3" button
        homepage.click_product_page_three_button()
        expected_results_text = "Showing 33–37 of 37 results"
        actual_results_text = homepage.get_product_results_text()
        self.assertEqual(expected_results_text, actual_results_text)

        time.sleep(2)

        # Toggle back to results page 2 using "2" button
        homepage.click_product_page_two_button()
        expected_results_text = "Showing 17–32 of 37 results"
        actual_results_text = homepage.get_product_results_text()
        self.assertEqual(expected_results_text, actual_results_text)

        time.sleep(2)

        # Toggle back to results page 1 using "1" button
        homepage.click_product_page_one_button()
        expected_results_text = "Showing 1–16 of 37 results"
        actual_results_text = homepage.get_product_results_text()
        self.assertEqual(expected_results_text, actual_results_text)

    @classmethod
    def tearDown(cls):
        cls.browser.close()
        cls.browser.quit()
        print('Test Completed')