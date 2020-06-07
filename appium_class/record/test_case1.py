#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

author: whiteP

modified time: 2020/5/17 12:00

"""

# coding=utf-8
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'  # 手机系统版本
desired_caps['deviceName'] = 'device'  # 刚才的devicename
desired_caps['appPackage'] = 'com.android.settings'  # 计算器的package
desired_caps['appActivity'] = 'com.android.settings.Settings'  # 计算器的activity

driver = webdriver.Remote('http://localhost:4723/wd/hub',
                          desired_caps)  # 运行该脚本desired_caps
time.sleep(3)  # 在计算器页面等待3秒
print('连接成功')  # 控制台输出“连接成功”

driver.quit()
