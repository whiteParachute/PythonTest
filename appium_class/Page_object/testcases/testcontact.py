#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

author: whiteP

modified time: 2020/6/7 14:18

"""
import pytest
import yaml

from appium_class.Page_object.page.app import App


class TestAddContact():
    def setup(self):
        self.main = App().start().main()

    @pytest.mark.parametrize("username, gender, phonenum", yaml.safe_load(
        open("../data/contact.yml", encoding="utf-8")))
    def test_addcontact(self, username, gender, phonenum):
        self.main.goto_addresslist().click_addmember().click_menualadd(). \
            input_username(username).set_gender(gender). \
            input_phone(phonenum).click_save().verify_toast().click_back()
