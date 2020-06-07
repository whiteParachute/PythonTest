#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

author: whiteP

modified time: 2020/6/7 14:12

"""
from appium.webdriver.common.mobileby import MobileBy

from appium_class.Page_object.page.base_page import BasePage


# from appium_class.Page_object.page.memberinvitepage import MemberInvitePage


class AddressListPage(BasePage):
    def click_addmember(self):
        from appium_class.Page_object.page.memberinvitepage import \
            MemberInvitePage

        # 滚动查找 添加成员
        self.find(MobileBy.ANDROID_UIAUTOMATOR,
                  'new UiScrollable(new UiSelector().'
                  'scrollable(true).instance(0)).'
                  'scrollIntoView(new UiSelector().'
                  'text("添加成员").instance(0));').click()
        return MemberInvitePage(self._driver)
