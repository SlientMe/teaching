# -*- coding: utf-8 -*-
# @Time : 2019/10/14 16:59
# @Author : liuqi
# @FileName: printTest.py
# @Software: PyCharm
import time
print(time.time())
days = 365
for i in range(days):
    print("#",end="",flush=True)
    print('\r',"进度：{0}%".format(round((i+1)*100/days)),end="",flush=True)
    #     print('\r',"进度：%d%%"%(round((i+1)*100/days)),end="",flush=True)
    time.sleep(0.1)