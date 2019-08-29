# -*- coding: utf-8 -*-
# @Time : 2019/7/15 19:02
# @Author : liuqi
# @FileName: requestTest.py
# @Software: PyCharm
import requests

target = "http://llvbb.cn"
req = requests.get(url=target)
print(req.text)