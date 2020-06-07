#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

author: whiteP

modified time: 2020/5/31 22:26

"""
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Test_Delete():
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        desired_caps['noReset'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',
                                       desired_caps)
        self.driver.implicitly_wait(5)

    @pytest.fixture()
    def add_fixture(self):
        yield
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gu_"). \
            click()

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("username", [
        ("whiteP5"),
        ("whiteP6"),
        ("whiteP7")
    ])
    def test_case(self, add_fixture, username):
        # 进入通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 滚动查找 需要删除的成员
        self.driver.find_element(MobileBy.XPATH,
                                 f"//*[contains(@text, '{username}')]").click()
        # 点击右上角更多
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/guk") \
            .click()
        # 验证进入正确页面(如果抓到上一个页面的current_activity可以增加sleep)
        current_act = self.driver.current_activity
        assert \
            ".contact.controller.ContactDetailSettingActivity" in current_act

        # 点击编辑成员
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/azd") \
            .click()
        # 点击删除成员
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/duq") \
            .click()

        # 点击确定
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b_4") \
            .click()

        sleep(4)
        assert username not in self.driver.page_source
