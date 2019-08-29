html_doc = """"
<html><head><title>The Dormouse‘s story</title></head>
<body>
<p class=“title”><b>The Dormouse‘s story</b></p>
<p class=“story”>
Once upon a time there were three little sisters; and their names were:
<a href=“http://example.com/elsie” class=“sister” id=“link1”>Elsie</a>,
<a href=“http://example.com/lacie” class=“sister” id=“link2”>Lacie</a> and
<a href=“http://example.com/tillie” class=“sister” id=“link3”>Tillie</a>,
and they lived at the bottom of a well.</p>
<p class=“story”>...</p>
"""


# from bs4 import BeautifulSoup, NavigableString
# soup = BeautifulSoup(html_doc,'html.parser')
#
# s = soup.body.contents[3]
# st = ''
# for i in s.descendants:
#     if type(i) == NavigableString:
#         st += i
# st = st.replace("\n", "")
# print(st)


import requests
import bs4

url = 'https://so.gushiwen.org/mingju//'
req = requests.get(url)
soup = bs4.BeautifulSoup(req.text, 'html.parser')
lst = soup.find_all('a', {'target': '_blank'})
for i in lst:
    print(i.string)