from bs4 import BeautifulSoup
import lxml
import requests

# 好的网站  http://www.jsphp.net/python/show-24-214-1.html

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 1. 创建 beautifulsoup 对象： bs 在使用时需要指定一个“解析器”：
soup = BeautifulSoup(html,'lxml')  #创建 beautifulsoup 对象  lxml- 解析速度快，需额外安装
soup = BeautifulSoup(html,'html.parser')  #创建 beautifulsoup 对象

# soup1 = BeautifulSoup(open('index.html'),'html.parser')  #用本地 HTML 文件来创建对象
# print(soup.prettify())  #打印 soup 对象的内容，格式化输出
print(soup.p)
"""
2.  四种对象
Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:
Tag         NavigableString     BeautifulSoup   Comment

（1）Tag    Tag就是 HTML 中的一个个标签，例如：
print soup.title  这种方式查找的是在所有内容中的第一个符合要求的标签。
对于 Tag，它有两个重要的属性，name 和 attrs ：
print soup.title.name
print soup.p.attrs #在这里，我们把 p 标签的所有属性打印输出了出来，得到的类型是一个字典。
print soup.p['class'] #单独获取某个属性
print soup.p.get('class') ##单独获取某个属性 跟上面一样的
可以对这些属性和内容等等进行修改：    soup.p['class']="newClass"
可以对这个属性进行删除：        del soup.p['class']

（2）NavigableString
得到了标签的内容用 .string 即可获取标签内部的文字，例如：
print soup.p.string

（3）BeautifulSoup
BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag，
我们可以分别获取它的类型，名称：
print type(soup.name)
#<type 'unicode'>
print soup.name 
# [document]
print soup.attrs 
#{} 空字典

（4）Comment
Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号。我们找一个带注释的标签：
print soup.a
print soup.a.string
print type(soup.a.string)

3.   遍历文档树

（1）直接子节点
tag 的 .content 属性可以将tag的子节点以列表的方式输出：
print soup.html.contents  #输出方式为列表，我们可以用列表索引来获取它的某一个元素：
print soup.html.contents[0]  #用列表索引来获取它的某一个元素：

.children   它返回的不是一个 list，不过我们可以通过遍历获取所有子节点
for item in  soup.body.children:
    print item

（2）所有子孙节点
.contents 和 .children 属性仅包含tag的直接子节点，.descendants 属性可以对所有tag的子孙节点
进行递归循环，和 children类似，要获取其中的内容，我们需要对其进行遍历：
for item in soup.descendants:
    print item
    
（3）节点内容
如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。如果标签里面只
有唯一的一个标签了，那么 .string 也会返回最里面的内容：
如果tag包含了多个子节点,tag就无法确定，string 方法应该调用哪个子节点的内容, .string 的输出结果是 None：

（4）多个内容  .strings 获取多个内容，不过需要遍历获取，比如下面的例子：
for string in soup.strings:
    print(repr(string))
输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容：
for string in soup.stripped_strings:
    print(repr(string))
    
（5）父节点
content = soup.head.title.string
print content.parent.name

（7）兄弟节点
兄弟节点可以理解为和本节点处在统一级的节点，.next_sibling 属性获取了该节点的
下一个兄弟节点，.previous_sibling 属性获取了该节点的上一个兄弟节点，如果节点不存在，则返回 None

（8）全部兄弟节点
通过 .next_siblings 和 .previous_siblings 属性可以对当前节点的兄弟节点迭代输出：
for sibling in soup.a.next_siblings:
    print(repr(sibling))

4.  搜索文档树
find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
    A.传字符串
soup.find_all('b')  name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉
    C.传列表
如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.下面代码找到文档中所有<a>标签和<b>标签：
soup.find_all(["a", "b"])
    D keyword 参数
    如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,
    如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性：
soup.find_all(id='link2')
soup.find_all("a", class_="sister")
使用 limit 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.
soup.find_all("a", limit=2)

5.  CSS选择器
在这里我们也可以利用类似的方法来筛选元素，用到的方法是 soup.select()，返回类型是 list
（1）通过标签名查找
print soup.select('title') 
print soup.select('a')
（2）通过类名查找
print soup.select('.sister')
（3）通过 id 名查找
print soup.select('#link1')
（4）组合查找
例如查找 p 标签中，id 等于 link1的内容，二者需要用空格分开：
print soup.select('p #link1')
（5）属性查找
print soup.select('a[class="sister"]')
print soup.select('p a[href="http://example.com/elsie"]')


















"""
