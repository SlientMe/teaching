'''
#### 练习1：实现计算求最大公约数和最小公倍数的函数。

```Python
def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    return x * y // gcd(x, y)

太极
#-*- coding:utf-8 -*-
import turtle

def yin(radius, color1, color2):
    # t.width(3)
    t.color("black", color1)
    t.begin_fill()
    t.circle(radius/2, 180)
    t.circle(radius, 180)
    t.left(180)
    t.circle(-radius/2, 180)
    t.end_fill()

    t.left(90)
    t.up()
    t.fd(radius * 0.35)
    t.right(90)
    t.down()
    t.color(color1, color2)
    t.begin_fill()
    t.circle(radius * 0.15)
    t.end_fill()
    t.left(90)
    t.up()
    t.bk(radius * 0.35)
    t.down()
    t.left(90)

def main():
    t.reset()
    yin(200, 'black', 'white')
    yin(200, 'white', 'black')

if __name__ == "__main__":
    t = turtle.Turtle()
    main()
    print("hello, vipJr")
    turtle.mainloop()

'''