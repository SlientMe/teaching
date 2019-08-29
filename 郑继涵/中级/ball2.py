# -*- coding: utf-8 -*-

# Py之pygame：有趣好玩——利用pygame库实现一个移动底座弹球的小游戏

import pygame as pg
from pygame.locals import *  # 将pygame所有常量导入，如后面的QUIT
from time import sleep
import sys

# 设置基本屏幕参数
pg.init()  # 初始化，如果没有的话字体会报错等等
scr = pg.display.set_mode((600, 550))  # 设置屏幕大小
pg.display.set_caption(("移动底座弹球的小游戏"))  # 设置屏幕标题
pp = 255, 255, 0  # red是一个元组，表示乒乓球橙色
green = 0, 255, 0
white = 255, 255, 255
dizuo = 120, 63, 4  # 底座颜色灰土色
pink = 255, 0, 255
cs = 225, 121, 21  # 乒乓球颜色，橙色

# 设计一下乒乓球的运动方式，乒乓球在屏幕内运动
x = 120  # 乒乓球的坐标设置为(x,y)
y = 120
vx = 3  # 设置初速度vx，vy，当乒乓球到达屏幕边缘的时候速度取反，也就是乒乓球到达左右两边缘的时候vx取反，上下边缘的时候vy取反。
vy = 3
a = 200  # a代表乒乓板的x坐标值，因为乒乓板y坐标值是固定的

My_font = pg.font.Font(None, 40)  # 40是字的大小，设置字体，None表示没有，代指pygame默认的字体，但是这样的字体缺点是不能打印出中文。
zt1 = pg.font.SysFont('华文楷体', 24)  # 楷体，a=pg.font.get_fonts()  #获得系统自带的字体
zt2 = pg.font.SysFont('华文楷体', 20)
zt21 = pg.font.SysFont('幼圆', 29)


def printtext(font, text, x, y, color):  # 设计一个函数，在游戏屏幕上打印文本,代码表示先把文本转换成一个位图然后打印在屏幕上，打印文本需要打印的具体坐标和文本颜色，字体等参数。
    img = font.render(text, True, color)  # 转换为位图
    scr.blit(img, (x, y))


# 设置得分，基础记分量，为什么设置基础记分量？我想的是经过一段时间后乒乓球会加速，从而逐渐增加游戏难度，当然，基础记分量也要翻倍。
c = 0  # c是加速器，如果接了10次，那么加速
fs = 0  # fs是分数，接到一次乒乓球就加分
k = 1  # 基础加分量

# 游戏的主要代码了，pygame采用帧和轮询的方式，帧是指会不断刷新，也就是while True循环，轮询是不断的询问用户的输入。
# 在下面代码中，会不断获取鼠标具体坐标和QUIT事件是否发生。Scr.fill会用RGB值为(199,21,133)的颜色刷新屏幕，
# 以后画圆写字都在这基础上，下一次循环后又刷新。因此在屏幕中乒乓球和乒乓板就会动态呈现出来。
while True:
    scr.fill((199, 21, 133))  # 游戏背景色
    # background = pg.image.load('./img/background.png').convert()
    # scr.blit(background, (0, 0))
    for eve in pg.event.get():
        if eve.type == QUIT:  # 点击左上角的×
            sys.exit()  # 如果无效，可以试试exit()函数
    mx, my = pg.mouse.get_pos()  # 获得鼠标的x，y坐标
    a = mx  # 鼠标x坐标就是乒乓板的坐标，因此移动鼠标乒乓板也移动
    # 画乒乓球和画乒乓板了，我们可以简化为圆形和矩形
    pg.draw.circle(scr, pp, (x, y), 40, 0)
    pg.draw.rect(scr, dizuo, (a, 530, 100, 20), 0)
    # 考虑乒乓球的运动，如果乒乓球碰到左右屏幕边缘，vx取反，碰到上边缘或者碰到乒乓板的时候，vy取反，其余情况表示乒乓板没有接触到乒乓球，跳出循环，游戏结束。
    x = x + vx
    y = y + vy
    if x > 550 or x < 40:
        vx = -vx
    if y < 40:
        vy = -vy
    if y > 510 and abs(a - x + 50) < 50:
        if vy > 0:
            vy = -vy
        else:
            pass
        c = c + 1  # 每接到3次后乒乓球加速
        fs = fs + k  # 加分
        if c >= 3:
            c = 0
            k = k + k  # 乒乓球加速后记分量双倍
            if vx > 0:  # 加速
                vx = vx + 1
            else:
                vx = vx - 1
        else:
            pass
    elif y > 510 and abs(a - x + 50) > 50:
        break
    # 在while循环最后，我写一下得分，规则，还有刷新，刷新很重要！
    sleep(0.005)  # 休眠一定时间，不然乒乓球速度依然很快
    printtext(zt21, "移动鼠标控制底座左右移动", 120, 20, pink)
    printtext(zt2, "得分", 550, 12, green)
    printtext(zt2, str(fs), 560, 32, green)
    pg.display.update()
# 在循环结束后就是前面乒乓板没有接触到乒乓球后发生的情况，最后是游戏结束的代码，毕竟这游戏靠看得分看成败
scr.fill((28, 69, 135))  # 游戏结束后全屏改变颜色
zt3 = pg.font.SysFont('华文楷体', 60)
zt4 = pg.font.SysFont('华文楷体', 40)
printtext(zt3, "你好，游戏结束", 60, 120, white)
printtext(zt4, '总得分: ' + str(fs), 120, 400, white)
pg.display.update()
