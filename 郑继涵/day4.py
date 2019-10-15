import turtle

color = input("请输入颜色")  # "#000000"  十六进制
turtle.pensize(5)        #画笔宽度
turtle.pencolor(color)  #修改画笔颜色，也可以用这种方式turtle.pencolor(1,1,1)
turtle.speed(1)           #画笔的速度
turtle.forward(-100)
turtle.mainloop()

'''
a + b 输出结果： HelloPython
a * 2 输出结果： HelloHello
a[1] 输出结果： e
a[1:4] 输出结果： ell   索引是从0开始的，画方格让学生理解
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

-------------------------------------------------------------------------------------------------------------

input函数的使用(小转换):
    ```Python
    """
    将华氏温度转换为摄氏温度
    F = 1.8C + 32
    
    Version: 0.1
    Author: 骆昊
    """
    f = float(input('请输入华氏温度: '))
    c = (f - 32) / 1.8
    print('%.1f华氏度 = %.1f摄氏度' % (f, c))
    ```



#########################################################################################################################
输入半径计算圆的周长和面积

Version: 0.1
Author: 骆昊
"""

import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)

--------------------------------------------------------------------------------------------------------------
in	成员运算符 - 如果字符串中包含给定的字符返回 True	'H' in a 输出结果 True
not in	成员运算符 - 如果字符串中不包含给定的字符返回 True

len()
print(name.split("."))  # 列表
print(len(name.split(".")))



讲解颜色RGB的组成， 讲解颜色的组成  pencolor（#feda23）

作业：
用户输入颜色，绘制出用户输入颜色的五角星

'''