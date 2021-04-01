from django.test import TestCase
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

class TestProjectListPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser=webdriver.Chrome('function_tests/chromedriver.exe')

    def tearDown(self): 
        self.browser.close()

    def home_buy_test(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.browser.maximize_window()
        time.sleep(1)
        self.browser.find_element_by_class_name("abc").click()
        time.sleep(5)

    def home_sell_test(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.browser.maximize_window()
        self.browser.find_element_by_class_name("def").click()
        time.sleep(5)
    
    def home_search_test(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.browser.maximize_window()
        self.browser.find_element_by_name("query").send_keys("Car")
        time.sleep(2)
        self.browser.find_element_by_class_name("efg").click()
        time.sleep(5)
    