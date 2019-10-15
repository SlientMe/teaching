# -*- coding: utf-8 -*-
# @Time : 2019/8/2 19:13
# @Author : liuqi
# @FileName: day10.py
# @Software: PyCharm

'''

练习题

1. 生成任意多个随机数，并升序排列

import random
s = []
for i in range(int(input())):
    s.append(random.randint(1, 1000))
print(sorted(s))
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


1、元素分类

1有如下值集合 [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
 2即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}

 li = [11,22,33,44,55,66,77,88,99,90]
dic = {
    "k1":[],
    "k2":[],
}
for i in li :
    if i <=66 :
        dic['k1'].append(i)
    else :
        dic['k2'].append(i)
print(dic)

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

统计单词次数
统计s='hello alex alex say hello sb sb'

s='hello alex alex say hello sb sb'

l=s.split()
dic={}
for item in l:
    if item in dic:
        dic[item]+=1
    else:
        dic[item]=1
print(dic)

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!
数字重复统计:
    1)随机生成1000个整数;
    2)数字范围[20,100];
    3)升序输出所有不同的数字及其每个数字重复的次数
代码：
import random
# 1.随机生成1000个在20-100范围内的数字
nums = []
for i in range(1000):
    num = int(random.randint(20,100))
    nums.append(num)
# print(nums)
# 2.排序(升序)
sort_nums = sorted(nums)
# 3.存入字典，key--随机生成的数字，value--重复的次数
dict = {}
for i in  sort_nums:
     if i not in dict:
         dict[i] = 1
     else:
         dict[i] += 1
print(dict)
---------------------

重复的单词: 此处认为单词之间以空格为分隔符， 并且不包含，和.；
    # 1. 用户输入一句英文句子；
    # 2. 打印出每个单词及其重复的次数;
例如:
输入:
   "hello java hello python"

输出:
   hello 2
   java 1
   python 1

# 1.接收用户输入一句英文句子
sentence = input('sentence:')
# print(sentence.split(' '))
# 2.将接收的英文句子分离
split_sentence = sentence.split(' ')
# 3.存入字典，key--每个单词 value--每个单词重复的次数
dict = {}
for i in  split_sentence:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

# 4.按要求输出
for key,value in dict.items():
    print(key,value)
---------------------


# 单词检查机
dict = {"test":"测试","name":"姓名"}
while True:
    a = input("a")

    if a in dict:
        print(dict[a])
    else:
        print("no exsit")

"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

'''