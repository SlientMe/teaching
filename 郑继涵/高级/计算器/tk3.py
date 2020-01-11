# 绝对布局
import tkinter

win = tkinter.Tk()
win.title("yudanqu")
win.geometry("400x400+200+50")

# label1 = tkinter.Label(win, text="good", bg="blue").pack(side='left')
label1 = tkinter.Label(win, text="good", bg="blue")
label2 = tkinter.Label(win, text="nice", bg="red")
label3 = tkinter.Label(win, text="cool", bg="green")
label4 = tkinter.Label(win, text="handsome", bg="yellow")

# 绝对布局，窗口的变化对位置没有影响
# label1.place(x=10,y=10，anchor='nw)
# label2.place(x=50,y=50)
# label3.place(x=100,y=100)

# 相对布局，窗体改变对控件有影响
# label1.pack(fill=tkinter.Y, side=tkinter.LEFT)
# label2.pack(fill=tkinter.X, side=tkinter.TOP)
# label3.pack()

 # 表格布局
 # 外部扩展 设置每个单元格的宽度
# label1.grid(row=0,column=0,padx=10,pady=10)
# 内部扩展 设置每个单元格的宽度
# label1.grid(row=0,column=0,ipadx=10,ipady=10)
# label1.grid(row=0,column=0)
# label2.grid(row=0,column=1)
# label3.grid(row=1,column=0)
# label4.grid(row=1,column=1)

win.mainloop()