
from model.group import Group
from conftest import app


def test_modify_name(app):
    app.group.modify_first_group(Group(name = "New group"))

def test_modify_header(app):
    app.group.modify_first_group(Group(header="New header"))
