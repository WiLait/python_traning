
from model.group import Group
from conftest import app


def test_modify_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name = "New group"))
    app.session.logout()


def test_modify_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="New header"))
    app.session.logout()
