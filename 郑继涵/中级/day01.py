'''


先 让学生写一个 两个数的阶乘 相加
m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fmn = 1

print(fm +fn )

让学生定义使用看看
语法
Python 定义函数使用 def 关键字，一般格式如下：

def 函数名（参数列表）:
    函数体

def hello() :
   print("Hello World!")
hello()

讲解函数的四种不同形式

   有无参数  有无返回值

让学生定义使用


写一个让两几个数相加的函数
def roll_dice(n=2):

    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


# 计算面积函数
def area(width, height):
    return width * height
def print_welcome(name):
    print("Welcome", name)
print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))
'''