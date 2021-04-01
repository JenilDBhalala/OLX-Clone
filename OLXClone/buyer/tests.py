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

    def buy_Item_test(self):
        self.browser.get('http://127.0.0.1:8000/buyer/buyItem/')
        self.browser.find_element_by_name("query1").send_keys("Car")
        self.browser.maximize_window() 
        time.sleep(2)
        self.browser.find_element_by_name("min_price").send_keys("5000")
        time.sleep(1)
        self.browser.find_element_by_name("max_price").send_keys("500000")
        time.sleep(2)
        self.browser.find_element_by_class_name("abc").click()
        time.sleep(5)
    