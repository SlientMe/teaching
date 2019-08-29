# -*- coding: utf-8 -*-
# @Time : 2019/7/29 18:45
# @Author : liuqi
# @FileName: day09.py
# @Software: PyCharm
poem = '''
桃花坞里桃花庵，桃花庵下桃花仙。
桃花仙人种桃树，又摘桃花换酒钱。
酒醒只在花前坐，酒醉还来花下眠。
酒醉酒醒日复日，花开花落年复年。
但愿老死花酒间，不愿鞠躬车马前。
车尘马足富者趣，酒盏花枝贫者缘。
若将富贵比贫贱，一在平地一在天。
若将花酒比车马，他得驱驰我得闲。
别人笑我忒疯癫，我笑他人看不穿。
不见五陵豪杰墓，无花无酒锄作田。
'''

'''
count = 0
for i in poem:
    if i== "花":
        count = count+1
        print(count)

replace
temp_str = 'this is a test'
print(temp_str.replace('is','IS')
print(temp_str)

while

string.isalnum()
如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False

string.isalpha()
如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False

string.isdigit()
如果 string 只包含数字则返回 True 否则返回 False.

string.isspace()
如果 string 中只包含空格，则返回 True，否则返回 False.

max(str)
返回字符串 str 中最大的字母。

min(str)
返回字符串 str 中最小的字母。
'''


'''



import random

print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数  
print( random.random() )             # 产生 0 到 1 之间的随机浮点数
print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数
'''

''''

=========================================================================

Python列表
List（列表） 是 Python 中使用最频繁的数据类型。

列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。

列表用 [ ] 标识，是 python 最通用的复合数据类型。


list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个元素 
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表

更新列表
list = ['Google', 'Runoob', 1997, 2000]
 
print ("第三个元素为 : ", list[2])
list[2] = 2001
print ("更新后的第三个元素为 : ", list[2])

删除列表的元素
del list[2]
print ("删除第三个元素 : ", list)


len([1, 2, 3])	3	长度
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
3 in [1, 2, 3]	True	元素是否存在于列表中
for x in [1, 2, 3]: print(x, end=" ")	1 2 3	迭代

方法：
！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
1	list.append(obj)
在列表末尾添加新的对象
2	list.count(obj)
统计某个元素在列表中出现的次数
3	list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
将对象插入列表
6	list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
移除列表中某个值的第一个匹配项
8	list.reverse()
反向列表中元素
9	list.sort( key=None, reverse=False)
对原列表进行排序
10	list.clear()
清空列表
11	list.copy()
复制列表
！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！

li = ['alex', 'aric', 'rain']
# 计算列表的长度
print(len(li))

# 列表中追加元素‘seven',并输出添加后的列表
li.append('seven')
print(li)

# 请在列表第一个元素插入'Tony'
li.insert(0,'Tony')   # 根据索引插入元素
print(li)

# 请修改列表中第二个位置的元素为‘kelly',并输出修改后的列表
li.pop(1)
li.insert(1,'kelly')
print(li)

# 请删除列表中的’eric',并输出修改后的列表
a = li.index('aric')    # 查找‘Eric’的位置
li.pop(a)               # 按索引删除
print(li)

# 请删除列表中的第二个值，请输出删除的值和删除后的列表
a = li.pop(1)       # 按索引删除，并用a接受删除值
print(a,li)

# 请删除列表中的第三个值，并输出删除后的列表
li.pop(2)
del li[2]
li.remove('rain')
print(li)

# 请删除列表中的第2个到第4个元素，并输出删除后的列表
li.extend([1, 3])
print(li)
del li[1:4:1]
print(li)

# 请将列表中的值反转，请输出反转后的列表
print(li[::-1])

# 请使用for,len,range输出列表的索引
for i in range(len(li)):
    print(i)

# 请使用enumr ate输出列表的元素和序号
for i,j in enumerate(li):
    print(i,j)

# 请使用for循环列表中所有元素
for i in li:
    print(i)
    
    
应用：
比如定义2个同学： 
姓名：李明，年龄23，考试分数：语文80，数学75，英语85   可以直接 % 元祖输出
姓名：张强，年龄25，考试分数：语文75，数学82，英语78 

2.通过迭代遍历，在循环体内部，针对列表中的每一项元素，执行相同的操作。

3  li = 'asdasd'
new_li = list(li)
print(li)

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
1回顾昨天的操作
2随机生成一个随机数列表  列表中的列表

3设计一个程序，用来实现帮助小学生进行百以内的算术练习，它具有以
下功能：
提供10道加、减、乘或除四种基本算术运算的题目；
练习者根据显示的题目输入自己的答案，程序自动判断输入的答案是否
正确并显示出相应的信息。
import random
count = 0
right = 0
while count <= 10:
    # 创建列表，用来记录加减乘除四大运算符
    op = ['+', '-', '*', '/']
    # 随机生成op列表中的字符
    s = random.choice(op)
    a = random.randint(0,100)
    # 除数不能为0
    b = random.randint(1,100)
    print('%d %s %d = ' %(a,s,b))
    question = input('请输入您的答案:(q退出)')
    if s == '+':
        result = a + b
    elif s == '-':
        result = a - b
    elif s == '*':
        result = a * b
    else:
        result = a / b
    if question == str(result):
        print('回答正确')
        right += 1
        count += 1
    elif question == 'q':
         break
    else:
        print('回答错误')
        count+=1
# 计算正确率
if count == 0:
    percent = 0
else:
    percent = right / count

print('测试结束,共回答%d道题,回答正确个数为%d,正确率为%.2f%%' %(count,right,percent*100))

4 用户输入月份,判断这个月是哪个季节
 
分析：
3，4，5月----春季  6，7，8----夏季   9，10，11---秋季  12，1，2----冬季 

# 接收用户输入的月份
month = int(input('month:'))

spring = [3,4,5]
summer = [6,7,8]
autom = [9,10,11]
winter = [12,1,2]
# 判断输入的月份属于哪个季节
if month in spring:
    print('%s月是春天' %(month))
elif month in summer:
    print('%s月是夏天' %(month))
elif month in autom:
    print('%s月是秋天' %(month))
elif month in winter:
    print('%s月是冬天' % (month))
else:
    print('请输入正确的月份')
--------------------- 

（1）系统里面有多个用户，用户的信息目前保存在列表里面
users = [‘root’,‘westos’]
passwd = [‘123’,‘456’]
（2） 用户登陆(判断用户登陆是否成功
1).判断用户是否存在
2).如果存在
1).判断用户密码是否正确
如果正确，登陆成功，推出循环
如果密码不正确，重新登陆，总共有三次机会登陆
3).如果用户不存在
重新登陆，总共有三次机会

users = ['root','westos']
passwords = ['123','456']

#尝试登录次数
trycount = 0

while trycount < 3:
    inuser = input('用户名: ')
    inpassword = input('密码: ')
  trycount += 1
 if inuser in users:
        index = users.index(inuser)
        password = passwords[index]
 if inpassword == password:
            print('%s登录成功' %(inuser))
            break
        else:
            print('%s登录失败 : 密码错误' %inuser)
    else:
        print('用户%s不存在' %inuser)
else:
    print('尝试超过三次，请稍后再试')
--------------------- 


======================================================================================
Python 元组
元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
元组是另一个数据类型，类似于 List（列表）。
但是元组不能二次赋值，相当于只读列表。

元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
 
print tuple               # 输出完整元组
print tuple[0]            # 输出元组的第一个元素
print tuple[1:3]          # 输出第二个至第四个（不包含）的元素 
print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2       # 输出元组两次
print tuple + tinytuple   # 打印组合的元组

以下是元组无效的，因为元组是不允许更新的。而列表是允许更新的：
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用

3.元组的常用方法
t = (1,2.3,True,‘westos’,‘westos’)
print(t.count(‘westos’))
print(t.index(2.3))
del tup;
print ("删除后的元组 tup : ")
	tuple(seq)
将列表转换为元组。


==================================================================================
'''

'''

Python 字典
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。

两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典用"{ }"标识。字典由索引(key)和它对应的值value组成。

键必须是唯一的，但值则不必。

值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。

一个简单的字典实例：

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
 
 
print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值

dict['Age'] = 8               # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息
 
 
 del dict['Name'] # 删除键 'Name'
popitem: 删除最后一个key-value值
item = service.popitem()
dict.clear()     # 清空字典
del dict         # 删除字典 

字典的增加

# 定义字典
service = {'http':80,'ftp':21,'ssh':22}
print(service)

# 若key值不存在,则添加对应的key-value值
service['mysql'] = 3306
print(service)
# 若key值存在,则更新对应的value值
service['http'] = 8080
print(service)


6 get 方法获取指定key对应的value值
service = {'http':80,'ftp':21,'ssh':22}
# key不存在,默认返回None
# key不存在,有default,则返回default
print(service.get('http'))
print(service.get('https'))
print(service.get('https',443))

7 判断指定的key是否存在
if 'https' in service:
    print(service['https'])
else:
    print('key not exist')




字典内置函数&方法
Python字典包含了以下内置函数：
1	len(dict)
计算字典元素个数，即键的总数。	
>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> len(dict)
3
2	str(dict)
输出字典，以可打印的字符串表示。	
>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> str(dict)
"{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"
3	type(variable)
返回输入的变量类型，如果变量是字典就返回字典类型。	
>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> type(dict)
<class 'dict'>



Python字典包含了以下内置方法：

1	radiansdict.clear()
删除字典内所有元素
2	radiansdict.copy()
返回一个字典的浅复制
3	radiansdict.fromkeys()
创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	radiansdict.get(key, default=None)
返回指定键的值，如果值不在字典中返回default值
5	key in dict
如果键在字典dict里返回true，否则返回false
6	radiansdict.items()
以列表返回可遍历的(键, 值) 元组数组
7	radiansdict.keys()
返回一个迭代器，可以使用 list() 来转换为列表
8	radiansdict.setdefault(key, default=None)
和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	radiansdict.update(dict2)
把字典dict2的键/值对更新到dict里
10	radiansdict.values()
返回一个迭代器，可以使用 list() 来转换为列表
11	pop(key[,default])
删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
12	popitem()
随机返回并删除字典中的一对键和值(一般删除末尾对)。



# 请循环输出所有的key和value
for i in dic:
    print(i,dic[i])
    
遍历字典的key值：

# 定义字典
d = {'1':'a','2':'b'}

# 默认遍历字典的key值
for i in d:
    print(i)
#  keys：key值
for key in d.keys():
    print(key)
    
遍历字典的value值：
d = {'1':'a','2':'b'}

for value in d.values():
    print(value)
'''