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
print(os.cpu_count())


'''
isdir(path)   判断指定路径是否存在且是一个目录
isfile(path)   判断指定路径是否存在且是一个文件

makedirs(path)      递归创建多层目录
remove(path)     删除文件
rmdir(path)      删除单层目录，如该目录非空则抛出异常
removedirs(path)   递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常
rename(old, new)    将文件old重命名为new
os.sep        输出操作系统特定的路径分隔符（Win下为'\\'，Linux下为'/'）
split(path)    分割文件名与路径，返回(f_path, f_name)元组。如果完全使用目录，
                它也会将最后一个目录作为文件名分离，且不会判断文件或者目录是否存在
splitext(path)   分离文件名与扩展名，返回(f_name, f_extension)元组
getsize(file)       返回指定文件的尺寸，单位是字节


# 获取当前进程ID
print(os.getpid())
# 获取当前进程的父进程ID
print(os.getppid())
# 返回当前系统的CPU数量
print(os.cpu_count())

'''


