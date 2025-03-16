# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
        app.session.login("admin", "secret")
        app.group.create(Group(name="sai", header="ydfghd", footer="dhryftd"))
        app.session.logout()

def test_add_empty_group(app):
        app.session.login("admin", "secret")
        app.group.create(Group(name="", header="", footer=""))
        app.session.logout()

