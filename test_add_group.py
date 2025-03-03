# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from platformdirs import AppDirs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import pytest
from urllib3 import request

from application import Application
from group import Group
from application import Application

@pytest.fixture
def app():
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
        app.login("admin", "secret")
        app.create_group(Group(name="sai", header="ydfghd", footer="dhryftd"))
        app.logout()

def test_add_empty_group(app):
        app.login("admin", "secret")
        app.create_group(Group(name="", header="", footer=""))
        app.logout()

if __name__ == "__main__":
    unittest.main()