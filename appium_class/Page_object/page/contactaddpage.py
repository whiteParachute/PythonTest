#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

author: whiteP

modified time: 2020/6/7 14:14

"""
from appium.webdriver.common.mobileby import MobileBy

from appium_class.Page_object.page.base_page import BasePage


# from appium_class.Page_object.page.memberinvitepage import MemberInvitePage


class ContactAddPage(BasePage):
    def input_username(self, username):
        self.find(MobileBy.XPATH,
                  "//*[contains(@text, '姓名')]/..//*[@resource"
                  "-id='com.tencent.wework:id/au0']") \
            .send_keys(username)
        return self

    def set_gender(self, gender):
        self.find(MobileBy.XPATH,
                  "//*[@text='性别']/..//*[@resource-id="
                  "'com.tencent.wework:id/aut']").click()
        if gender == "男":
            self.find(MobileBy.ANDROID_UIAUTOMATOR,
                      'new UiSelector().text("男")').click()
        else:
            self.find(MobileBy.ANDROID_UIAUTOMATOR,
                      'new UiSelector().text("女")').click()
        return self

    def input_phone(self, phonenum):
        self.find(MobileBy.ID, "com.tencent.wework:id/eq7") \
            .send_keys(phonenum)
        return self

    def click_save(self):
        from appium_class.Page_object.page.memberinvitepage import \
            MemberInvitePage
        self.find(MobileBy.ID, "com.tencent.wework:id/gur") \
            .click()
        return MemberInvitePage(self._driver)
