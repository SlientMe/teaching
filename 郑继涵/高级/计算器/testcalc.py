import tkinter


# 定义计算器类
class Calc:
    # 初始化魔术方法
    def __init__(self):
        # 初始化共用属性
        # 定义一个用于存放被计算字符串的列表
        self.operationList = []
        # 定义运算标记 确定是否输入了运算符号
        self.isOper = False
        # 初始化界面
        self.initWindows()

    # 更改按键盘颜色方法
    def changeBg(self, evt):
        evt.widget['bg'] = 'cyan'

    # 恢复按键盘颜色方法
    def backBg(self, evt):
        evt.widget['bg'] = 'lightgray'


    # 界面布局方法
    def initWindows(self):
        # 生成主窗口 定制窗口尺寸
        root = tkinter.Tk()
        root.geometry("400x500")
        root.title('计算器')
        # 生成用于保存数值的变量
        self.num = tkinter.StringVar()
        self.num.set(0)

        # 运算结果输出位置
        result = tkinter.Label(root, width=20, height=2, bg='white', bd=10, anchor='e', font=('宋体', 50),
                               textvariable=self.num)

        result.place(relx=0, rely=0, relwidth=1.0, relheight=0.4)
        # result.pack()

        ###########################以下为按键部分############################
        buttonCE = tkinter.Button(root, text='CE', bg='lightgray')
        buttonCE.place(relx=0, rely=0.4, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        buttonCE.bind('<Enter>', self.changeBg)
        buttonCE.bind('<Leave>', self.backBg)

        buttonC = tkinter.Button(root, text='C', bg='lightgray')
        buttonC.place(relx=0.25, rely=0.4, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        buttonC.bind('<Enter>', self.changeBg)
        buttonC.bind('<Leave>', self.backBg)

        buttonDel = tkinter.Button(root, text='<-', bg='lightgray')
        buttonDel.place(relx=0.5, rely=0.4, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        buttonDel.bind('<Enter>', self.changeBg)
        buttonDel.bind('<Leave>', self.backBg)

        buttonDiv = tkinter.Button(root, text='÷', bg='lightgray')
        buttonDiv.place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        buttonDiv.bind('<Enter>', self.changeBg)
        buttonDiv.bind('<Leave>', self.backBg)

        button1 = tkinter.Button(root, text='1', bg='lightgray')
        button1.place(relx=0, rely=0.5, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button1.bind('<Enter>', self.changeBg)
        button1.bind('<Leave>', self.backBg)

        button2 = tkinter.Button(root, text='2', bg='lightgray')
        button2.place(relx=0.25, rely=0.5, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button2.bind('<Enter>', self.changeBg)
        button2.bind('<Leave>', self.backBg)

        button3 = tkinter.Button(root, text='3', bg='lightgray')
        button3.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button3.bind('<Enter>', self.changeBg)
        button3.bind('<Leave>', self.backBg)

        buttonX = tkinter.Button(root, text='x', bg='lightgray')
        buttonX.place(relx=0.75, rely=0.5, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        buttonX.bind('<Enter>', self.changeBg)
        buttonX.bind('<Leave>', self.backBg)

        button4 = tkinter.Button(root, text='4', bg='lightgray',)
        button4.place(relx=0, rely=0.6, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button4.bind('<Enter>', self.changeBg)
        button4.bind('<Leave>', self.backBg)

        button5 = tkinter.Button(root, text='5', bg='lightgray')
        button5.place(relx=0.25, rely=0.6, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button5.bind('<Enter>', self.changeBg)
        button5.bind('<Leave>', self.backBg)

        button6 = tkinter.Button(root, text='6', bg='lightgray')
        button6.place(relx=0.5, rely=0.6, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button6.bind('<Enter>', self.changeBg)
        button6.bind('<Leave>', self.backBg)

        button_ = tkinter.Button(root, text='-', bg='lightgray')
        button_.place(relx=0.75, rely=0.6, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button_.bind('<Enter>', self.changeBg)
        button_.bind('<Leave>', self.backBg)

        button7 = tkinter.Button(root, text='7', bg='lightgray')
        button7.place(relx=0, rely=0.7, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button7.bind('<Enter>', self.changeBg)
        button7.bind('<Leave>', self.backBg)

        button8 = tkinter.Button(root, text='8', bg='lightgray')
        button8.place(relx=0.25, rely=0.7, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button8.bind('<Enter>', self.changeBg)
        button8.bind('<Leave>', self.backBg)

        button9 = tkinter.Button(root, text='9', bg='lightgray')
        button9.place(relx=0.5, rely=0.7, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button9.bind('<Enter>', self.changeBg)
        button9.bind('<Leave>', self.backBg)

        buttonAdd = tkinter.Button(root, text='+', bg='lightgray')
        buttonAdd.place(relx=0.75, rely=0.7, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        buttonAdd.bind('<Enter>', self.changeBg)
        buttonAdd.bind('<Leave>', self.backBg)

        buttonFlag = tkinter.Button(root, text='±', bg='lightgray')
        buttonFlag.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        buttonFlag.bind('<Enter>', self.changeBg)
        buttonFlag.bind('<Leave>', self.backBg)

        button0 = tkinter.Button(root, text='0', bg='lightgray')
        button0.place(relx=0.25, rely=0.8, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button0.bind('<Enter>', self.changeBg)
        button0.bind('<Leave>', self.backBg)

        buttonPoint = tkinter.Button(root, text='.', bg='lightgray')
        buttonPoint.place(relx=0.5, rely=0.8, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        buttonPoint.bind('<Enter>', self.changeBg)
        buttonPoint.bind('<Leave>', self.backBg)

        buttonEque = tkinter.Button(root, text='=', bg='lightgray')
        buttonEque.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        buttonEque.bind('<Enter>', self.changeBg)
        buttonEque.bind('<Leave>', self.backBg)
        #########################以上为按键部分############################
        # # 底部显示信息
        # bottomLabel = tkinter.Label(root, text='Power By Microhard Corpration\n@2017'
        #                             , bg='cyan', width=30, height=1, padx=0)
        # bottomLabel.place(relx=0, rely=0.9, relwidth=1.0, relheight=0.1)

        # 主窗口循环
        root.mainloop()


# 实例化计算器对象
c = Calc()