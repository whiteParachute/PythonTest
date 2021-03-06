"""

author: whiteP

modified time: 2020/4/12 11:46

"""

# Generated by Selenium IDE
import json
import time
from typing import List, Dict

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test123():
    def setup_method(self, method):
        # 打开浏览器debug模式，连接到debug模式端口
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_opts)
        # self.driver = webdriver.Chrome()

        # 打开企业微信页面
        self.driver.get("https://work.weixin.qq.com/")
        # 隐士等待
        self.driver.implicitly_wait(3)

    def teardown_method(self, method):
        self.driver.quit()

    def test_123(self):
        # self.driver.get("https://work.weixin.qq.com/")
        # self.driver.find_element(By.CSS_SELECTOR,
        #                          ".index_service_cnt_item_title").click()
        # time.sleep(15)
        # 记录cookies
        cookies = self.driver.get_cookies()
        with open("cookies.txt", "w") as f:
            json.dump(cookies, f)
        # 读取cookies
        with open("cookies.txt", "r") as f:
            cookies: List[Dict] = json.load(f)
        for cookie in cookies:
            # 忽略expiry
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        # 自动登录后进入主页面点击“添加成员”bottom
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.index_service_cnt_itemWrap').click()
        # self.driver.find_element(By.CSS_SELECTOR, "#username").\
        #     send_keys("hello")
        # self.driver.find_element(By.XPATH, '//*[@id="memberAdd_acctid"]').\
        #     send_keys("hello2")
