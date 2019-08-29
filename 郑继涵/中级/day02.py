# -*- coding: utf-8 -*-
# @Time : 2019/8/14 20:39
# @Author : liuqi
# @FileName: day02.py
# @Software: PyCharm

'''
写出一个函数，封装一下
渐变色
import turtle
turtle.pensize(3)
turtle.pencolor("red")
turtle.speed(9)
for i in range(100):
    turtle.pencolor(i/100, i/100, i/100)
    for j in range(4):
        if j == 1:
            turtle.pendown()
        else:
            turtle.penup()
        turtle.forward(i)
        turtle.left(90)
turtle.mainloop()


写出一个函数，封装一下
平行线
import turtle
turtle.pensize(3)
turtle.pencolor("red")
for i in range(4):
    if i==1 or i==3:
        turtle.penup()
    else :
        turtle.pendown()
    turtle.forward(100)
    turtle.right(90)
turtle.mainloop()



全局变量和局部变量
定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。

total = 0 # 这是一个全局变量                   # 统计函数调用了多少次
# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total

sum( 10, 20 )
print ("函数外是全局变量 : ", total)

我们可以使用`global`关键字来指示`foo`函数中的变量`a`来自于全局作用域，
如果全局作用域中没有`a`，那么下面一行的代码就会定义变量`a`并将其置于全局作用域。
同理，如果我们希望函数内部的函数能够修改嵌套作用域中的变量，可以使用`nonlocal`关键字来指示变量来自于嵌套作用域，请大家自行试验。

def foo():
    global a
    a = 200
    print(a)  # 200
a = 100
foo()
print(a)  # 200

计算次方
def power(x, n):   默认2次方
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

默认参数
调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值：
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
#调用printinfo函数
printinfo( age=50, name="runoob" )
print ("------------------------")
printinfo( name="runoob" )
！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！

不定长参数  *vartuple 列表 元祖    **vartuple   字典
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下：

def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
printinfo( 70, 60, 50 )
！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！



python 传不可变对象实例
实例(Python 3.0+)
#!/usr/bin/python3
def ChangeInt( a ):
    a = 10
b = 2
ChangeInt(b)
print( b ) # 结果是 2
！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！

传可变对象实例
可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist)
   return

# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)


=# 即在调用add函数时可以传入0个或多个参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))

函数的重写
```Python
def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')


# 下面的代码会输出什么呢？
foo()


多边形画图封装一下

```
'''
