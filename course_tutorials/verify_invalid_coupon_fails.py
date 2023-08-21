from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


def open_browser():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(5)
    return driver

def go_to_home_page(driver):
    driver.get('http://demostore.supersqa.com')

def add_first_item_to_cart(driver):
    first_add_btn = driver.find_element(By.CLASS_NAME, 'add_to_cart_button')
    first_add_btn.click()

def go_to_cart_page(driver):
    driver.get('http://demostore.supersqa.com/cart')

def apply_coupon(driver, coupon_code):
    coupon_field = driver.find_element(By.ID, 'coupon_code')
    coupon_field.send_keys(coupon_code)
    apply_btn = driver.find_element(By.CSS_SELECTOR, 'button.button:nth-child(3)')
    apply_btn.click()

def verify_cart_has_item(driver):

    for i in range(5):
        try:
            driver.find_element(By.CLASS_NAME, 'cart_item')
            return
        except NoSuchElementException:
            print("Item not in cart. Retrying after 2 seconds")
            time.sleep(2)
            driver.refresh()

def get_displayed_error_message(driver):
    return driver.find_element(By.CSS_SELECTOR, '.woocommerce-error > li:nth-child(1)').text



if __name__ == '__main__':

    driver = open_browser()
    go_to_home_page(driver)
    add_first_item_to_cart(driver)
    go_to_cart_page(driver)
    verify_cart_has_item(driver)
    apply_coupon(driver, 'fakeone')
    get_displayed_error_message(driver)
    err_msg = get_displayed_error_message(driver)
    exp_msg = 'Coupon "fakeone" does not exist!'
    assert err_msg == exp_msg, f"Unexpected err message: {err_msg}"
    print('PASS')
    # driver.quit()