#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

author: whiteP

modified time: 2020/6/7 14:09

"""
from appium.webdriver.common.mobileby import MobileBy

from appium_class.Page_object.page.addresslistpage import AddressListPage
from appium_class.Page_object.page.base_page import BasePage


class Main(BasePage):
    def goto_message(self):
        pass

    def goto_addresslist(self):
        # self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.steps("../steps/mainsteps.yml")
        return AddressListPage(self._driver)

    def goto_workbench(self):
        pass

    def goto_profile(self):
        pass
