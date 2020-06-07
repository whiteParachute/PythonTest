#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

author: whiteP

modified time: 2020/5/24 15:57

"""
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Test_Wework():
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

    # def setup(self):
    #     pass
    #
    # def teardown(self):
    #     self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gu_"). \
    #         click()

    @pytest.fixture()
    def add_fixture(self):
        yield
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gu_"). \
            click()

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("username, gender, phonenum", [
        ("whiteP1", "男", "13800001112"),
        ("whiteP2", "男", "13800001113"),
        ("whiteP3", "男", "13800001114"),
        ("whiteP4", "女", "13800001115"),
        ("whiteP5", "女", "13800001116"),
        ("whiteP6", "女", "13800001117"),
        ("whiteP7", "女", "13800001118")
    ])
    def test_case(self, add_fixture, username, gender, phonenum):
        # 进入通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 滚动查找 添加成员
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        # 点击手动输入添加
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/c7g"). \
            click()
        # 验证进入正确页面(如果抓到上一个页面的current_activity可以增加sleep)
        current_act = self.driver.current_activity
        assert ".contact.controller.ContactAddActivity" in current_act

        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '姓名')]/..//*[@resource"
                                 "-id='com.tencent.wework:id/au0']") \
            .send_keys(username)
        # 选择性别
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='性别']/..//*[@resource-id="
                                 "'com.tencent.wework:id/aut']").click()
        if gender == "男":
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                     'new UiSelector().text("男")').click()
        else:
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                     'new UiSelector().text("女")').click()
        # 输入手机号
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/eq7") \
            .send_keys(phonenum)
        # 点击保存
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gur") \
            .click()

        sleep(2)
        # print(self.driver.page_source)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")
        # assert "添加成功" in self.driver.find_element\
        #     (MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
