import tkinter as tk

##第1步，实例化object，建立窗口window
window = tk.Tk()
# 第2步，给窗口的可视化起名字
window.title("test")
# 第3步，设定窗口的大小(长 * 宽)
window.geometry("500x500+200+300")   # 这里的乘号是小x

# window.resizable(0,0)                 # 设置主窗口的宽度和高度是否可以通过鼠标进行拉伸改变，此处设置为不能
var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
# StringVar()是Tk库内部定义的字符串变量类型，可以用它来显示计算内容，set()用来改变值，get()用来获取值。
var.set("Test")
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=10, height=2)
# l.pack()
l.place(relx = 0,rely = 0,relwidth = 1.0)  # Label内容content区域放置位置，自动调节尺寸

on_hit = False
def hit_me(test):
    print(test)
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')


b = tk.Button(window, text='hi', font=('Arial', 12), width=10, height=1, command=lambda:hit_me(1))
# b.place(relx = 0,rely = 0.2,relwidth = 1.0)
b.grid(row=1, column=1)

window.mainloop()
