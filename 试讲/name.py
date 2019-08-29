from turtle import *

# turtle.write("你的名字", move=False, align="left", font=("Arial", 8, "normal"))
import binascii

KEYS = [0x80, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02, 0x01]
ht()
screensize()

Turtle().screen.delay(0)  # 输出无延时
Turtle().screen.colormode(255)  # 设置颜色为255格式

rect_list = [] * 16
for i in range(16):
    rect_list.append([] * 16)

text = "你的名字"


def filled_rectangle(x: int, y: int, l: int, w: int, colorGray: int):  # 画出正方形
    up()
    goto(x, y)
    pencolor((128 - colorGray) // 2, (128 - colorGray) // 2, (128 - colorGray) // 2)
    fillcolor(((128 - colorGray) // 2, (128 - colorGray) // 2, (128 - colorGray) // 2))
    down()
    begin_fill()
    for i in range(2):
        right(90)
        forward(l)
        right(90)
        forward(w)
    end_fill()


def printBitMap(char: str, x: int, y: int, fontSize: int):
    gb2312 = char.encode('gb2312')
    hex_str = binascii.b2a_hex(gb2312)
    result = str(hex_str, encoding='utf-8')
    area = eval('0x' + result[:2]) - 0xA0
    index = eval('0x' + result[2:]) - 0xA0
    offset = (94 * (area - 1) + (index - 1)) * 32
    font_rect = None
    with open("HZK16", "rb") as f:  # 打开HZK16文件添加到Buffer
        f.seek(offset)
        font_rect = f.read(32)
    rect_list = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]  # 清空列表
    for k in range(len(font_rect) // 2):
        row_list = rect_list[k]
        for j in range(2):
            for i in range(8):
                asc = font_rect[k * 2 + j]
                flag = asc & KEYS[i]
                row_list.append(flag)  # 将字体文件转为列表矩阵

    for row in range(len(rect_list)):
        for col in range(len(rect_list[row])):
            if rect_list[row][col]:
                filled_rectangle(x + col * fontSize, y - row * fontSize, fontSize, fontSize, rect_list[row][col])


def printText(text: str, x: int, y: int, fontSize: int):  # 输出若干个文字
    width_screen = window_width()
    height_screen = window_height()
    for index, enum in enumerate(text):
        printBitMap(enum, x - width_screen / 2 + fontSize * 16 * index, -y + height_screen / 2, fontSize)