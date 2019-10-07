import os
print(os.getcwd())
os.chdir("C://")
print(os.getcwd())
try:
    os.mkdir(os.getcwd()+"/test")
except:
    print("文件已存在时，无法创建该文件")
print(os.path.isdir(os.getcwd()))

# os.path.isfile(“e:\\1.txt”)  #判断该””内的对象是否是文件，如果是则返回True，不是则为False
# os.makedirs(“e:\\1\\2\\3\\4\\5”)  #递归创建目录 （递归增加多个目录）
# os.remove(“e:\\1.txt”)  #删除e盘下的TXT文件 （删除文件）
# os.remove("e:\\1\\2\\3\\4\\5\\1.txt")  #删除多级目录下的TXT文件（只能删除文件）
# os.removedirs(“e:\\1\\2\\3\\4\\5”) #递归从右侧至左侧删除e盘下的目录，如果某一级目录非空，那么停止删除（删除多级目录）
# os.rename(“e:\\a.py”,”b.py”)  #指定目录下重命名文件（改文件操作）
# os.rename(“e:\\1”,”e:\\2”)  #指定目录重命名  （改目录操作）
# os.listdir(os.getcwd())  #当前路径下的所有文件和目录 （查看当前目录下文件）
# os.listdir(“e:\\”)   #指定目录下的所有文件和目录  （查看当前目录下文件）
# os.path.exists()  #检验给出的路径是否真地存:
# os.path.getsize（filename） #获取文件大小

'''
统计某一级目录下的文件和目录数

import os
import os.path
os.chdir("e:\\1software")
print os.getcwd()
dir_result = 0
file_result =0
for i in os.listdir(os.getcwd()):
    if  os.path.isdir(i):
        dir_result+=1
    else:
        file_result+=1
print dir_result,file_result


统计某个特定目录项目的特定文件，比如MP3文件  .py文件（通过对os.listdir，然后切分字符串，可以得到后缀）
或者可以使用os.path.splitext()  #分离扩展名


用代码实现创建5级目录
l  方法一：

import os
os.chdir("e:\\1software")
print os.getcwd()
for i in range(1,6):
    os.mkdir(str(i))
    os.chdir(str(i))

l  方法二：
import os
os.makedirs("e:\\photo\\2\\3\\4\\5\\6")

'''


