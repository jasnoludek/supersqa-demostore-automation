from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pdb

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('http://demostore.supersqa.com')

# by "id"
cart = driver.find_element(By.ID, "site-header-cart")
print(cart)
print(type(cart))
cart_txt = cart.text
print(cart_txt)

# by "id"
search_field = driver.find_element(By.ID, "woocommerce-product-search-field-0")
search_field.send_keys("Hoodie")
search_field.send_keys(Keys.ENTER)

#by css selector
my_acct = driver.find_element(By.CSS_SELECTOR, ".nav-menu > li:nth-child(4)")
my_acct.click()

pdb.set_trace()


driver.quit()
driver.close()