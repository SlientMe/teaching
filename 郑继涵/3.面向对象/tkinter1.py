import tkinter as tk

##第1步，实例化object，建立窗口window
window = tk.Tk()
# 第2步，给窗口的可视化起名字
window.title("test")
# 第3步，设定窗口的大小(长 * 宽)
window.geometry("500x500+200+300")   # 这里的乘号是小x

window.resizable(0,0)                 # 设置主窗口的宽度和高度是否可以通过鼠标进行拉伸改变，此处设置为不能



# # 第4步，在图形界面上设定标签
# l = tk.Label(window, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=30, height=2)
# # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
'''
在 Tkinter 中，Label 控件用以显示文字和图片。本程序用了两个Label分别来显示计算过程和计算结果，本次用到的参数有：
label = tkinter.Label(root, font=('微软雅黑', 20), bg='#EEE9E9', bd='9', fg='#828282', anchor='se', textvariable=result2)
font	设置字体跟文字大小
bg	设置背景颜色
bd	指定Label的边框宽度
fg	设置Label的文本和位图的颜色
anchor	控制文本（或图像）在Label中显示位置
n,ne,e,se,s,sw,w,nw,或center来定位（ewsn代表东西南北，上北下南左西右东）
textvariable	Label显示Tkinter变量（通常是一个StringVar变量）的内容
最后用place()来设置位置和大小。
'''
#
# # 第5步，放置标签
# l.pack()  # Label内容content区域放置位置，自动调节尺寸
# # 放置lable的方法有：1）l.pack(); 2)l.place();

# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
# StringVar()是Tk库内部定义的字符串变量类型，可以用它来显示计算内容，set()用来改变值，get()用来获取值。

l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

# 第6步，在窗口界面设置放置Button按键
b = tk.Button(window, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
b.pack()



# 第6步，主窗口循环显示
window.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键


'''
Entry是tkinter类中提供的的一个单行文本输入域，用来输入显示一行文本，收集键盘输入(类似 HTML 中的 text)。
什么时候用：需要用户输入用户信息时，比如我们平时使用软件、登录网页时，用户交互界面让我们登录账户信息等时候可以用到。

# 第4步，在图形界面上设定输入框控件entry并放置控件
e1 = tk.Entry(window, show='*', font=('Arial', 14))   # 显示成密文形式
e2 = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式
e1.pack()
e2.pack()

'''