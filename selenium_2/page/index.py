"""

author: whiteP

modified time: 2020/4/19 16:45

"""
from selenium.webdriver.common.by import By

from selenium_2.page.base_page import BasePage
from selenium_2.page.register import Register


class Index(BasePage):
    # 进入注册页
    def goto_register(self):
        self.driver.get("https://work.weixin.qq.com/")
        # 点击立即注册按键
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".index_head_info_pCDownloadBtn").click()
        # 进入到注册页
        return Register(self.driver)
        pass

    # 进入登录页
    def goto_login(self):
        pass
