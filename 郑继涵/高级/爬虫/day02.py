from bs4 import BeautifulSoup
import requests

url = 'http://python123.io/ws/demo.html'
r = requests.get(url)
# print(r)
# print(r.content)
demo = r.text  # 服务器返回响应
print(demo)

soup = BeautifulSoup(demo, "html.parser")
"""
demo 表示被解析的html格式的内容
html.parser表示解析用的解析器
"""
# print(soup)  # 输出响应的html对象
print(soup.prettify())  # 使用prettify()格式化显示输出
#（1）
print(soup.title)  # 获取html的title标签的信息
print(soup.a)  # 获取html的a标签的信息(soup.a默认获取第一个a标签，想获取全部就用for循环去遍历)
print(soup.a.name)   # 获取a标签的名字
print(soup.a.parent.name)   # a标签的父标签(上一级标签)的名字
print(soup.a.parent.parent.name)  # a标签的父标签的父标签的名字
# （2）
print('a标签类型是：', type(soup.a))   # 查看a标签的类型
print('第一个a标签的属性是：', soup.a.attrs)  # 获取a标签的所有属性(注意到格式是字典)
print('a标签属性的类型是：', type(soup.a.attrs))  # 查看a标签属性的类型
print('a标签的class属性是：', soup.a.attrs['class'])   # 因为是字典，通过字典的方式获取a标签的class属性
print('a标签的href属性是：', soup.a.attrs['href'])   # 同样，通过字典的方式获取a标签的href属性
# （3）
print('第一个a标签的内容是：', soup.a.string)  # a标签的非属性字符串信息，表示尖括号之间的那部分字符串
print('a标签的非属性字符串的类型是：', type(soup.a.string))  # 查看标签string字符串的类型
print('第一个p标签的内容是：', soup.p.string)  # p标签的字符串信息(注意p标签中还有个b标签，
# 但是打印string时并未打印b标签，说明string类型是可跨越多个标签层次)

# 介绍一下find_all()方法：
'''
• name：对标签名称的检索字符串
• attrs：对标签属性值的检索字符串，可标注属性检索
• recursive：是否对子孙全部检索，默认True
• string：<>…</>中字符串区域的检索字符串 
'''

