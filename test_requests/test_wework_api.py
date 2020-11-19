#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

author: whiteP

modified time: 2020/11/19 20:04

"""
import json

import requests


class TestWeworkApi:
    def test_wework_api(self):
        secret = 'NEMJxYC66nU9OD4aZoKVKvyunf3Ut6oVPUrD0JWiwQI'
        id = 'wwc44512a924a7349f'

        def setup(self):
            r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/"
                             "gettoken?corpid={id}&corpsecret="
                             "{secret}")
            print(r.json())
            self.token = r.json()["access_token"]

        def testone(self):
            r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/"
                             "department/list?access_token={self.token}&id=2")
            if r.json()["errcode"] != 0:
                create_json = {
                    "name": "成都",
                    "name_en": "CD",
                    "parentid": 1,
                    "order": 1,
                    "id": 2
                }
                a = json.dumps(create_json, ensure_ascii=False)
                b = json.loads(a)
                r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/"
                                  "department/create?access_token={self.token}",
                                  json=b)
                print(r.json())
                update_json = {
                    "id": 2,
                    "name": "成都修改",
                    "name_en": "CD",
                    "parentid": 1,
                    "order": 1
                }
                r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/"
                                  "department/update?access_token={self.token}",
                                  json=update_json)
                print(r.json())
            else:
                r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/"
                                 "department/delete?access_token="
                                 "{self.token}&id=2")
                print(r.json())
