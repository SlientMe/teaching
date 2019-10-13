''''

import shutil
# shutil.move()
shutil.copy2("test.txt","me.txt")

什么是异常？
异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。
一般情况下，在Python无法正常处理程序时就会发生一个异常。
异常是Python对象，表示一个错误。
当Python脚本发生异常时我们需要捕获处理它，否则程序会终止执行。

try:
    print(1/0)
except Exception:
    print()

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()



异常捕获
    try:
        f = open('致橡树.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()

使用except而不带任何异常类型
你可以不带任何异常类型使用except，如下实例：

try:
    正常的操作
   ......................
except:
    发生异常，执行这块代码
   ......................
else:
    如果没有异常执行这块代码
    2222
'''

with open('test.txt','r',encoding='utf-8') as f:
    f.readline()
    print(f.readline())

'''
复制文件并打开
f1 = open("test.txt","r")
f2 = open("test1.txt","a+")
for i in f1:
    f2.write(i)
f2.seek(0)
print(f2.read())

f1.close()
f2.close()
'''

'''
print(f.tell())    返回当前文件指针的位置
seek() 方法语法如下：
fileObject.seek(offset[, whence])
offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。

# 查找当前位置
position = fo.tell()
print "当前文件位置 : ", position

们已经有一个音调文件了、usic.txt,里面是：
	do re mi fa so la si
1 2 3 4 5 6 7
	一共七个读音，我们希望在另一个文件中出现
	“do do so so la la so， fa fa mi mi re re do ”
	开始动手吧～ 
	算了 还是先给个例子吧～
	with open("test/music.txt", "rb+") as f1, open("test/demo.txt", "ab+") as f2:
    f2.write(f1.read(3))
    f1.seek(-3, 1)
    f2.write(f1.read(3))
    f1.seek(12)
    f2.write(f1.read(3))
    f1.seek(-3, 1)
    f2.write(f1.read(3))
    f2.write(f1.read(3))
    f1.seek(-3, 1)
    f2.write(f1.read(3))
    f1.seek(-6, 1)
    f2.write(f1.read(3))
	这时我们demo.txt里面就应该有do do so so la la so 了，你来把后面半句补上吧～


'''


'''
我们需要注意的是，每次读写完文件后都要记得close()关闭文件。
为了保证close()方法可以被顺利调用，我们可以使用try-finally来实现，
finally里面的代码不管有没有异常发生都会执行。
我们把close()方法放在finally就可以啦：
try:
    f = open(“test.txt”, “r”)
    print(f.read())
finally:
    if f:
        f.close()
但是如果每次都这样写其实是一件挺麻烦的事情，对吧？
python给我们提供了with语句来简化这种写法：
with open(“test.txt”, “r”) as f:
    print(f.read())

'''


