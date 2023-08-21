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

search_field_id = 'id-search-field'
search_field_elm = driver.find_element(By.ID, 'id-search-field')
search_field_elm.send_keys(('testing'))

go_btn_id = 'submit'
go_btn_elm = driver.find_element(By.ID, go_btn_id)
go_btn_elm.click()