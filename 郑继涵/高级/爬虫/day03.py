import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/cinema/nowplaying/xian/"

# def get_webInfo(url):
# 获取页面信息
response = requests.get(url=url)
content = response.text
# 分析页面，获取ID和电影名称
soup = BeautifulSoup(content, 'html.parser')
# 找到所有的电影信息对应的LI标签
movie_list = soup.find_all('li', class_='list-item')
# movie_list是一个可迭代对象
# print(type(movie_list))
# print(movie_list[0])
# 储存所有电影信息[{'title':'名称'，'id':'id号'}]
movies_info = []
# 依次遍历每一个li标签，提取所需要的信息
for item in movie_list:
    now_movies_dict = {}
    print(item)
    # 根据属性获取title和id内容
    # item['data-title']获取li标签里面的指定属性data-title对应的value值;
    now_movies_dict['title'] = item['data-title']
    now_movies_dict['id'] = item['id']
    now_movies_dict['actors'] = item['data-actors']
    now_movies_dict['director'] = item['data-director']
    # 将获取的{'title':"名称", "id":"id号"}添加到列表中;
    movies_info.append(now_movies_dict)
with open('movies.txt', 'w',encoding="utf-8") as f:
    for item in movies_info:
        f.write(str(item) + '\n')
