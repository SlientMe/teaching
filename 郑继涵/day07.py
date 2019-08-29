### 应用场景
'''

如果在程序中我们需要重复的执行某条或某些指令，例如用程序控制机器人踢足球，
如果机器人持球而且还没有进入射门范围，那么我们就要一直发出让机器人向球门方向奔跑的指令。
当然你可能已经注意到了，刚才的描述中其实不仅仅有需要重复的动作，还有我们上一个章节讲到的分支结构。
再举一个简单的例子，比如在我们的程序中要实现每隔1秒中在屏幕上打印一个&quot;hello, world&quot;
这样的字符串并持续一个小时，我们肯定不能够将`print('hello, world')`这句代码写上3600遍，如果真的需要这样做，
那么编程的工作就太无聊了。因此，我们还需要了解一下循环结构，有了循环结构我们就可以轻松的控制某件事或者某些事重复、重复、再重复的去执行。

在Python中构造循环结构有两种做法，一种是`for-in`循环，一种是`while`循环。

'''
# 先让学生画一个正方形
# for循环画出正方形，让学生体会一下

'''
用for循环实现1~100求和

sum = 0
for x in range(101):
    sum += x
print(sum)


n = int(input('n = '))
result = 1
for x in range(1, n + 1):
    result *= x
print('%d! = %d' % (n, result))

'''

'''
需要说明的是上面代码中的`range`类型，`range`可以用来产生一个不变的数值序列，而且这个序列通常都是用在循环中的，例如：

- `range(101)`可以产生一个0到100的整数序列。
- `range(1, 100)`可以产生一个1到99的整数序列。
- `range(1, 100, 2)`可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量。

'''


"""
用for循环实现1~100之间的偶数求和
sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)


sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)

"""


'''
循环填充颜色
import turtle
turtle.speed(0)
turtle.hideturtle()
for c in range(100):
    turtle.fillcolor(c/100, 0, 0)    # random.random()
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()

turtle.done()


打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Version: 0.1
Author: 骆昊
"""

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()

'''