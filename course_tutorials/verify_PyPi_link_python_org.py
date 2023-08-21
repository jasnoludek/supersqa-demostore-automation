from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('https://www.python.org/')

cur_title = driver.title
expected_title = 'Welcome to Python.org'

if cur_title != expected_title:
    raise Exception("Went to python.org but got wrong title. Current title: {}".format(cur_title))

pypi_header_link_locator = '.pypi-meta'
pypi_header_link_elm = driver.find_element(By.CSS_SELECTOR, pypi_header_link_locator)
pypi_header_link_elm.click()

cur_url = driver.current_url
expected_url = 'https://pypi.org/'
assert cur_url == expected_url, f"Clicked on PyPi but the url opened was: {cur_url}"
print("PASS")
# driver.quit()