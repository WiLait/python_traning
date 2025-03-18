# -*- coding: utf-8 -*-
from model.group import Group
from conftest import app

def test_add_group(app):
        app.group.create(Group(name="sai", header="ydfghd", footer="dhryftd"))

def test_add_empty_group(app):
        app.group.create(Group(name="", header="", footer=""))

