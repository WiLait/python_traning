# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False
class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.dw = WebDriver()
        self.dw.implicitly_wait(60)
    
    def test_add_group(self):
        dw = self.dw
        dw.get("http://localhost/addressbook/")
        dw.find_element(By.NAME,"user").click()
        dw.find_element(By.NAME,"user").clear()
        dw.find_element(By.NAME,"user").send_keys("admin")
        dw.find_element(By.NAME,"pass").click()
        dw.find_element(By.NAME,"pass").clear()
        dw.find_element(By.NAME,"pass").send_keys("secret")
        dw.find_element(By.XPATH,"//input[@value='Login']").click()
        dw.find_element(By.LINK_TEXT,"groups").click()
        dw.find_element(By.NAME,"new").click()
        dw.find_element(By.NAME,"group_name").click()
        dw.find_element(By.NAME,"group_name").clear()
        dw.find_element(By.NAME,"group_name").send_keys("sai")
        dw.find_element(By.NAME,"group_header").click()
        dw.find_element(By.NAME,"group_header").clear()
        dw.find_element(By.NAME,"group_header").send_keys("ydfghd")
        dw.find_element(By.NAME,"group_footer").click()
        dw.find_element(By.NAME,"group_footer").clear()
        dw.find_element(By.NAME,"group_footer").send_keys("dhryftd")
        dw.find_element(By.NAME,"submit").click()
        dw.find_element(By.LINK_TEXT,"group page").click()
        dw.find_element(By.LINK_TEXT,"Logout").click()
    
    def is_element_present(self, how, what):
        try: self.dw.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.dw.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.dw.quit()

if __name__ == "__main__":
    unittest.main()
