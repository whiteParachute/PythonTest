#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

author: whiteP

modified time: 2020/6/7 14:05

"""
from appium import webdriver

from appium_class.Page_object.page.base_page import BasePage
from appium_class.Page_object.page.main import Main


class App(BasePage):
    def start(self):
        # 启动app
        caps = {}
        caps['noReset'] = 'true'
        caps['platformName'] = 'Android'
        caps['platformVersion'] = '6.0'
        caps['deviceName'] = 'emulator-5554'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = '.launch.WwMainActivity'
        caps['autoGrantPermissions'] = 'true'
        self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self._driver.implicitly_wait(5)
        return self

    def stop(self):
        pass

    def restart(self):
        pass

    def main(self):
        return Main(self._driver)
