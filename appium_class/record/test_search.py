#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

author: whiteP

modified time: 2020/5/4 15:29

"""
from appium import webdriver


class Test_Wework():
    def setup(self):
        desired_caps = {}
        desired_caps['noReset'] = 'true'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['autoGrantPermissions'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',
                                       desired_caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_case(self):
        el1 = self.driver.find_element_by_id("com.tencent.wework:id/guu")
        el1.click()
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/fk1")
        el2.send_keys("zabcde")
        el2.click()
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/"
            "android.widget.LinearLayout/android.widget.FrameLayout/"
            "android.widget.RelativeLayout/android.widget.FrameLayout/"
            "android.widget.RelativeLayout/android.widget.FrameLayout/"
            "android.widget.ListView/android.widget.RelativeLayout[2]/"
            "android.widget.RelativeLayout/android.widget.RelativeLayout[1]/"
            "android.widget.RelativeLayout")
        el3.click()
