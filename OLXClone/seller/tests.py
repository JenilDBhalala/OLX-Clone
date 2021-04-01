from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.support.select import Select
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

class TestProjectListPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser=webdriver.Chrome('function_tests/chromedriver.exe')

    def tearDown(self): 
        self.browser.close()

    def add_Item_test(self):
        self.browser.get('http://127.0.0.1:8000/seller/addItem/')
        self.browser.maximize_window() 
        sel = Select(self.browser.find_element_by_xpath("//select[@name='category']"))
        sel.select_by_visible_text("Car")
        time.sleep(1)
        self.browser.find_element_by_name("item_name").send_keys("Car Hyundai")
        time.sleep(1)
        self.browser.find_element_by_name("price").send_keys("500000")
        time.sleep(1)
        self.browser.find_element_by_name("model_year").send_keys("2015")
        time.sleep(1)
        self.browser.find_element_by_name("model_year").send_keys("2015")
        time.sleep(1)
        sel = Select(self.browser.find_element_by_xpath("//select[@name='city']"))
        time.sleep(1)
        sel.select_by_visible_text("Vadodara")
        time.sleep(1)
        self.browser.find_element_by_name("area").send_keys("atladara")
        time.sleep(1)
        self.browser.find_element_by_xpath("//input[@type='file']").send_keys(r"C:\Users\Dell\Desktop\car.jpeg")
        time.sleep(1)
        self.browser.find_element_by_name("description").send_keys("Car is really good")
        time.sleep(1)
        self.browser.find_element_by_name("mo_no").send_keys("9563256463")
        time.sleep(1)
        self.browser.find_element_by_class_name("abc").click()
        time.sleep(10)
    
    def edit_Item_test(self):
        self.browser.get('http://127.0.0.1:8000/user/edit_item/42?csrfmiddlewaretoken=MCuvN9prB1RRbbDj4Wk6pIlXGabmJNEwVDS6iYxh4H4b0EVBvUVZq5tQ5xF2WPw6')
        self.browser.maximize_window() 
        sel = Select(self.browser.find_element_by_xpath("//select[@name='category']"))
        sel.select_by_visible_text("Car")
        time.sleep(1)
        self.browser.find_element_by_name("item_name").clear()
        self.browser.find_element_by_name("item_name").send_keys("Car Hyundai")
        time.sleep(1)
        self.browser.find_element_by_name("price").clear()
        self.browser.find_element_by_name("price").send_keys("250000")
        time.sleep(1)
        self.browser.find_element_by_name("model_year").clear()
        self.browser.find_element_by_name("model_year").send_keys("2015")
        time.sleep(1)
        sel = Select(self.browser.find_element_by_xpath("//select[@name='city']"))
        time.sleep(1)
        sel.select_by_visible_text("Vadodara")
        time.sleep(1)
        self.browser.find_element_by_name("area").clear()
        self.browser.find_element_by_name("area").send_keys("atladara")
        time.sleep(1)
        self.browser.find_element_by_xpath("//input[@type='file']").send_keys(r"C:\Users\Dell\Desktop\car.jpeg")
        time.sleep(1)
        self.browser.find_element_by_name("description").clear()
        self.browser.find_element_by_name("description").send_keys("Car is really good")
        time.sleep(1)
        self.browser.find_element_by_class_name("abc").click()
        time.sleep(10)