"""

author: whiteP

modified time: 2020/4/19 21:31

"""
from selenium.webdriver.common.by import By

from selenium_4.page.base_page import BasePage


class AddMember(BasePage):
    # 在添加成员页面实现输入内容并保存
    def add_member(self):
        # self.driver.find_element_by_id("username").send_keys("abcde")
        self.find(By.ID, "username").send_keys("zabcde")
        # self.driver.find_element_by_id("memberAdd_acctid").send_keys("fffff")
        self.find(By.ID, "memberAdd_acctid").send_keys("fffff")
        # self.driver.find_element_by_id("memberAdd_phone"). \
        #     send_keys("12345678910")
        self.find(By.ID, "memberAdd_phone").send_keys("12345678911")
        # # 点击保存
        # self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

    def get_first(self):
        # 找出符合要求的所有element
        elems = self.finds(By.CSS_SELECTOR, '#member_list td:nth-child(2)')
        arrs = []
        # 对所有element进行遍历
        for elem in elems:
            # 依次取出其中的title属性，并存入数组
            arrs.append(elem.get_attribute("title"))
        return arrs
