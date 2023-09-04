import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage


class TestSearchForHoodies(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_verify_search(self):
        browser = self.browser

        browser.get("http://demostore.supersqa.com/")

        homepage = HomePage(browser)

        homepage.search("hoodie")

        results = homepage.get_hoodie_search_results()
        count = len(results)
        assert count == 3

    @classmethod
    def tearDown(cls):
        cls.browser.close()
        cls.browser.quit()
        print('Test Completed')
