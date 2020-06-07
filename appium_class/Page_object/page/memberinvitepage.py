#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

author: whiteP

modified time: 2020/6/7 14:13

"""
# from appium_class.Page_object.page.addresslistpage import AddressListPage
from appium.webdriver.common.mobileby import MobileBy

from appium_class.Page_object.page.base_page import BasePage


# from appium_class.Page_object.page.contactaddpage import ContactAddPage


class MemberInvitePage(BasePage):
    def click_menualadd(self):
        from appium_class.Page_object.page.contactaddpage import ContactAddPage
        # 点击手动输入添加
        self.find(MobileBy.ID, "com.tencent.wework:id/c7g"). \
            click()
        return ContactAddPage(self._driver)

    def click_back(self):
        from appium_class.Page_object.page.addresslistpage import \
            AddressListPage
        return AddressListPage(self._driver)

    def verify_toast(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成功']")
        return self
