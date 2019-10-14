from PIL import Image  # 图像处理库 pillow（PIL）：
import argparse   # argparse 库是用来管理命令行参数输入的

'''
字符画是一系列字符的组合，我们可以把字符看作是比较大块的像素，一个字符能表现一种颜色（为了简化可以这么理解），字符的种类越多，
可以表现的颜色也越多，图片也会更有层次感。
问题来了，我们是要转换一张彩色的图片，这么多的颜色，要怎么对应到单色的字符画上去？这里就要介绍灰度值的概念了。

灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像。

另外一个概念是 RGB 色彩：

RGB色彩模式是工业界的一种颜色标准，是通过对红(R)、绿(G)、蓝(B)三个颜色通道的变化以及它们相互之间的叠加来得到各式各样的颜色的，
RGB即是代表红、绿、蓝三个通道的颜色，这个标准几乎包括了人类视力所能感知的所有颜色，是目前运用最广的颜色系统之一。- 来自百度百科介绍

我们可以使用灰度值公式将像素的 RGB 值映射到灰度值（注意这个公式并不是一个真实的算法，而是简化的 sRGB IEC61966-2.1 公式，
真实的公式更复杂一些，不过在我们的这个应用场景下并没有必要）：
gray ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b
这样就好办了，我们可以创建一个不重复的字符列表，灰度值小（暗）的用列表开头的符号，灰度值大（亮）的用列表末尾的符号。

'''

#命令行输入参数处理
parser = argparse.ArgumentParser()

'''
我们首先使用 argparse 处理命令行参数，目标是获取输入的图片路径、输出字符画的宽和高以及输出文件的路径：
'''
parser.add_argument('file')     #输入文件
parser.add_argument('-o', '--output')   #输出文件
parser.add_argument('--width', type = int, default = 80) #输出字符画宽
parser.add_argument('--height', type = int, default = 80) #输出字符画高

# 解析并获取参数
args = parser.parse_args()
# 输入的图片文件路径
IMG = args.file
# 输出字符画的宽度
WIDTH = args.width
# 输出字符画的高度
HEIGHT = args.height
# 输出字符画的路径
OUTPUT = args.output

# 首先将 RGB 值转为灰度值，然后使用灰度值映射到字符列表中的某个字符。
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#下面是 RGB 值转字符的函数，注意 alpha 值为 0 的时候表示图片中该位置为空白：
def get_char(r,g,b,alpha = 256):
    # 判断 alpha 值
    if alpha == 0:
        return ' '
    # 获取字符集的长度，这里为 70
    length = len(ascii_char)
    # 将 RGB 值转为灰度值 gray，灰度值范围为 0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    # 灰度值范围为 0-255，而字符集只有 70
    # 需要进行如下处理才能将灰度值映射到指定的字符上
    unit = (256.0 + 1)/length
    # 返回灰度值对应的字符
    return ascii_char[int(gray/unit)]

'''
图片的处理步骤如下：
1 .首先使用 PIL 的 Image.open 打开图片文件，获得对象 im
2. 使用 PIL 库的 im.resize() 调整图片大小对应到输出的字符画的宽度和高度，注意这个函数第二个参数使用 Image.NEAREST，表示输出低质量的图片。
3. 遍历提取图片中每行的像素的 RGB 值，调用 getchar 转成对应的字符
4. 将所有的像素对应的字符拼接在一起成为一个字符串 txt
5. 打印输出字符串 txt
6. 如果执行时配置了输出文件，将打开文件将 txt 输出到文件，如果没有，则默认输出到 output.txt 文件
'''

if __name__ == '__main__':
    # 打开并调整图片的宽和高
    im = Image.open(IMG)
    im = im.convert("RGBA")
    '''    RGB：3 元素元组      RGBA：4 元素元组        Gray （灰度图）：int 值   '''
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    # 初始化输出的字符串
    txt = ""
    '''
    im.getpixel((j,i)) 获取得到坐标 (j,i) 位置的 RGB 像素值（有的时候会包含 alpha 值），返回的结果是一个元组，
    例如 (1,2,3) 或者 (1,2,3,0)。我们使用 * 可以将元组作为参数传递给 get_char，同时元组中的每个元素都对应到 get_char 函数的每个参数。
    '''
    # 遍历图片中的每一行
    for i in range(HEIGHT):
        # 遍历该行中的每一列
        for j in range(WIDTH):
            # 将 (j,i) 坐标的 RGB 像素转为字符后添加到 txt 字符串
            txt += get_char(*im.getpixel((j, i)))
            '''
            返回的是一个元组，这个元组有三个元素，分别对应三个颜色通道（RGB）的值。
* 是一个运算符，对元组使用 * 运算符即为元组拆封操作。元组拆封会返回元祖的所有元素。
所以表达式 *im.getpixel((j,i)) 返回 3 个值，正好对应 get_char() 函数的三个参数。
            '''
            # 遍历完一行后需要增加换行符
        txt += '\n'
    # 输出到屏幕
    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)

# 运行  G:\githubRes\郑继涵\高级>python ptow.py wm.png