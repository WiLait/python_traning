#from fixture.session import SessionHelper
from conftest import app
#from selenium.webdriver.firefox.webdriver import WebDriver
#from fixture.group import GroupHelper
#from fixture.session import SessionHelper

def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()