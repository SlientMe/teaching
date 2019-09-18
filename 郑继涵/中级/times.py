import time
time.time()  # 1970纪元后经过的浮点秒数  时间戳(timestamp)的方式：通常来说，时间戳表示的是从1970年1月１日开始按秒计算的偏移量
print(time.localtime(time.time()))  #(2009, 2, 17, 10, 48, 39, 1, 48, 0)   时间元组
print(time.localtime(time.time()).tm_year)
# print time.tm_year


#获取格式化的时间
#str    print(time.asctime())   # 默认是本地时间即  time.localtime(time.time())
localtime = time.asctime( time.localtime(time.time()) )  # str
print(type(localtime))
print(localtime)


#格式化日期  time.strftime(format[, t])

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %M:%S",time.localtime()))
print(time.strftime("%m-%d"))

#python中时间日期格式化符号：
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）


#
# time.sleep(secs)
# 推迟调用线程的运行，secs的单位是秒

# import time
# t1 = time.clock()
# sum = 0
# for i in range(9999999):
#     sum = sum +1
# time.sleep(1)
# print(time.clock()-t1)

#  datatime

'''
练习我们以前讲过的递归
import datetime
import time
# sum =1
# for j in range(1,200):
#    sum = sum*j
def jiecheng(n):
    if n==1:
        return 1
    else:
        return  n*jiecheng(n-1)
jiecheng(200)
end = time.process_time()

print("%s" %(end))
'''

import datetime
a = datetime.date.today()
print(a)
print(a.year)
print(a.month)
print(a.day)

# 计算两个日期相差几天
d1 = datetime.date(2017, 3, 22)
d2 = datetime.date(2017, 3, 15)
d1.__sub__(d2)

'''
a = datetime.date(2017,3,22)
print(a.isoformat())     #'2017-03-22'

指定日期所在的星期数
a = datetime.date(2017,3,22)
print(a.isoweekday())


'''