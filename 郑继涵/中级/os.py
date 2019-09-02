import os
#Python的标准库中的os模块包含普遍的操作系统功能。如果你希望你的程序能够与平台无关的话，
# 这个模块是尤为重要的。即它允许一个程序在编写后不需要任何改动，也不会发生任何问题，就可以在Linux和Windows下运行。

'''
os.sep变量主要用于系统路径中的分隔符。
Windows系统通过是“\\”，Linux类系统如Ubuntu的分隔符是“/”，而苹果Mac OS系统中是“:”。
'''

# print(os.getcwd())   # 获取当前的目录

# os.mkdir(os.getcwd()+'/test')  # 创建新的目录

# os.chdir("C:/Users/Administrator/Desktop")  #必须是存在的，不然会报错  try except
# print(os.getcwd())   # 获取当前的目录

print(os.listdir())  #列出当前目录下的所有文件和文件夹。


