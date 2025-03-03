# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import unittest
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
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