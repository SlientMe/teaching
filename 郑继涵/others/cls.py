import requests
import bs4

url = 'https://so.gushiwen.org/mingju/'
req = requests.get(url)
soup = bs4.BeautifulSoup(req.text, 'html.parser')
lst = soup.find_all('a', target='_blank')
gushiwen = []
for i in lst:
    gushiwen.append(i.string)

with open('poems.txt', 'w') as f:
    f.writelines(gushiwen[1:-1])
