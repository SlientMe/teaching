# -*- coding: utf-8 -*-
# @Time : 2019/7/18 11:06
# @Author : liuqi
# @FileName: main.py
# @Software: PyCharm
from scrapy import cmdline

cmdline.execute('scrapy crawl douban_spider'.split())