from bs4 import BeautifulSoup
import requests

html = """
<!DOCTYPE html>
<html>
<head>
    <meta content="text/html;charset=utf-8" http-equiv="content-type" />
    <meta content="IE=Edge" http-equiv="X-UA-Compatible" />
    <meta content="always" name="referrer" />
    <link href="https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/bdorz/baidu.min.css" rel="stylesheet" type="text/css" />
    <title>百度一下，你就知道 </title>
</head>
<body link="#0000cc">
  <div id="wrapper">
    <div id="head">
        <div class="head_wrapper">
          <div id="u1">
            <a class="mnav" href="http://news.baidu.com" name="tj_trnews">新闻 </a>
            <a class="mnav" href="https://www.hao123.com" name="tj_trhao123">hao123 </a>
            <a class="mnav" href="http://map.baidu.com" name="tj_trmap">地图 </a>
            <a class="mnav" href="http://v.baidu.com" name="tj_trvideo">视频 </a>
            <a class="mnav" href="http://tieba.baidu.com" name="tj_trtieba">贴吧 </a>
            <a class="bri" href="//www.baidu.com/more/" name="tj_briicon" style="display: block;">更多产品 </a>
          </div>
        </div>
    </div>
  </div>
</body>
</html>
"""

# 1. 创建 beautifulsoup 对象：
bs = BeautifulSoup(html,'html.parser')  #创建 beautifulsoup 对象
# soup = BeautifulSoup(html,'lxml')  #创建 beautifulsoup 对象
# soup1 = BeautifulSoup(open('index.html'))  #用本地 HTML 文件来创建对象
# print(soup.prettify())  #打印 soup 对象的内容，格式化输出
# print(soup.p['class'])

# # print(soup.html.contents)
# # print(soup.html.children)
# allp = soup.find_all("p")
# for item in allp:
#     print(item[''])

print(bs.prettify()) # 获取title标签的所有内容
print(bs.title) # 获取title标签的名称
print(bs.title.name) # 获取title标签的文本内容
print(bs.title.string) # 获取head标签的所有内容

print(bs.div) # 获取第一个div标签的的值
print(bs.div["id"]) # 获取第一个a标签中的所有内容
print(bs.a) # 获取所有的a标签中的所有内容
print(bs.find_all("a")) # 获取id="u1"
for item in bs.find_all("a"):
    print(item.get("href")) # 获取所有的a标签，并遍历打印a标签的文本值

for item in bs.find_all("a"):
    print(item.get_text())
