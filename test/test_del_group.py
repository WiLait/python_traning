#from model.group import Group
from conftest import app

def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()