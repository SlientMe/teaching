import time
time.time()  # 1970纪元后经过的浮点秒数  时间戳(timestamp)的方式：通常来说，时间戳表示的是从1970年1月１日开始按秒计算的偏移量
print(time.localtime())  #(2009, 2, 17, 10, 48, 39, 1, 48, 0)   时间元组
print(time.localtime().tm_year)
# print time.tm_year


#获取格式化的时间
#str    print(time.asctime())   # 默认是本地时间即  time.localtime(time.time())
localtime = time.asctime( time.localtime(time.time()) )  # str
print(type(localtime))
print(localtime)


#格式化日期  time.strftime(format[, t])
# 比如我们换成2018-09-04 10:48:07的常见格式：
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


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
'''
import time
print(time.time())
days = 365
for i in range(days):
    print("#",end="",flush=True)
    print('\r',"进度：{0}%".format(round((i+1)*100/days)),end="",flush=True)
    #     print('\r',"进度：%d%%"%(round((i+1)*100/days)),end="",flush=True)
    time.sleep(0.1)
'''

#  datatime

'''
练习我们以前讲过的递归

import time
a1=time.perf_counter()
a2=time.process_time()
c=1
for i in range(1,20000):
    c*=i
b1=time.perf_counter()
b2=time.process_time()
print(b1-a1,'s')
print(b2-a2,'s')

perf_counter()会包含sleep()休眠时间，适用测量短持续时间
注意process_time()不包括sleep()休眠时间期间经过的时间。




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

'''
import calendar
print(calendar.calendar(2019))

# 2018年是平年，所以为False
print(calendar.isleap(2018))        # False
# 2008年是如年，所以为True
print(calendar.isleap(2008))        # True

prmonth(theyear, themonth, w=0, l=0)：打印一个月的日历，theyear指定年份，themonth指定月份，w每个单元格宽度，默认0，内部已做处理，最小宽度为2，l每列换l行，默认为0，内部已做处理，至少换行1行
calendar.month(2018, 8)

# 2008到2011之间只有2008年是闰年，所以数量为1  返回y1与y2年份之间的闰年数量
print(calendar.leapdays(2008, 2011))    # 1

weekday(year, month, day)：获取指定日期为星期几
print(calendar.weekday(2018, 8, 8))     # 2

weekheader(n)：返回包含星期的英文缩写，n表示英文缩写所占的宽度
print(calendar.weekheader(4))
############### 打印结果如下 ###############
Mon  Tue  Wed  Thu  Fri  Sat  Sun 

monthrange(year, month)：返回一个由一个月第一个天的星期与当前月的天数组成的元组
# 查看日历可以知道，08-01正是星期三，并且8月共31天
print(2018, 8)      # (2, 31)

from calendar import HTMLCalendar

c = HTMLCalendar(firstweekday=6)
print(c.formatmonth(2018, 8, withyear=False))


import datetime
import calendar
for i in range(2019,2029):
    print(datetime.datetime(i,1,1).strftime("%w"))
    print(calendar.weekday(i,1,1)+1)

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