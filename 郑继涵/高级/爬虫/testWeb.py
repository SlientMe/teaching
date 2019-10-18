from bs4 import BeautifulSoup
import requests

html = """
<html>
<head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>
</html>
"""

# 1. 创建 beautifulsoup 对象：
soup = BeautifulSoup(html,'html.parser')  #创建 beautifulsoup 对象
# soup = BeautifulSoup(html,'lxml')  #创建 beautifulsoup 对象
# soup1 = BeautifulSoup(open('index.html'))  #用本地 HTML 文件来创建对象
# print(soup.prettify())  #打印 soup 对象的内容，格式化输出
# print(soup.p['class'])

# print(soup.html.contents)
# print(soup.html.children)
allp = soup.find_all("p")
for item in allp:
    print(item[''])