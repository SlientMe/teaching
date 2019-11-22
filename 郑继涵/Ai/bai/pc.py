from bs4 import BeautifulSoup
import requests

url = 'https://so.gushiwen.org/shiwenv_affc7e5b993a.aspx'
r = requests.get(url)
# print(r)
# print(r.content)
demo = r.text  # 服务器返回响应

soup = BeautifulSoup(demo, "html.parser")
"""
demo 表示被解析的html格式的内容
html.parser表示解析用的解析器
"""
# print(soup)  # 输出响应的html对象
contetn = soup.find_all("div",class_="cont")
gushi = contetn[1]
print(gushi.h1.string)
poem = soup.find_all("div",id='contsonaffc7e5b993a')
print(poem[0].p.strings)
print(poem[0].p.contents)
for i in poem[0].p.strings:
    print(i)