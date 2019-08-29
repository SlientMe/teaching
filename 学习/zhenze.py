# -*- coding: utf-8 -*-
# @Time : 2019/7/15 18:50
# @Author : liuqi
# @FileName: zhenze.py
# @Software: PyCharm

import re
print(re.match('www', 'www.w3cschool.cn').span())  # 在起始位置匹配
print(re.match('cn', 'www.w3cschool.cn'))         # 不在起始位置匹配