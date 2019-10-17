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

    # 数字按钮操作方法
    def buttonAction(self, number):
        # 判断用户是否按下了运算按钮
        if self.isOper == True:
            # 在界面上显示运算符之后的数
            self.num.set(number)
            # 运算标记复位
            self.isOper = False
        else:
            # 没有铵下运算按钮
            # 判断原始界面数字是否为0
            existNumber = self.num.get()
            if existNumber == '0':
                # 如果界面中的初始数据为0 则获取用户输入数据并显示
                self.num.set(number)
            else:
                # 如果界面中的初始数据不为0 则对字符进行累加
                self.num.set(self.num.get() + number)

    # 运算按钮操作方法
    def operation(self, opFlag):
        # 运算标记置为真
        self.isOper = True
        # 获取界面中存在的数 并且写入列表
        self.operationList.append(self.num.get())
        # 当前运算符号不会在上一步中写入 需要单独写入
        self.operationList.append(opFlag)

    # 获取运行结果操作方法
    def getResult(self):
        # 将当前界面中数字加入计算列表
        self.operationList.append(self.num.get())
        # 开始计算
        result = eval(''.join(self.operationList))
        self.num.set(result)

    # 全部清空重新计算方法
    def clearAll(self):
        # 界面置0 计算列表置0
        self.num.set('0')
        self.operationList.clear()
        # 运算标志复位
        self.isOper = False

    # 实现退格键方法
    def backSpace(self):
        # 获取当前显示数字长度
        strLength = len(self.num.get())
        # 如果当前显示有数字
        if strLength > 1:
            # 删除字串中最后一个字
            presentStr = self.num.get()
            presentStr = presentStr[:strLength - 1]
            self.num.set(presentStr)
        else:
            self.num.set('0')

    # 正负号实现方法
    def pm(self):
        presentStr = self.num.get()
        # 实现增加和去除负号
        if presentStr[0] == '-':
            self.num.set(presentStr[1:])
        # 原始字串不得以-号和0开头
        elif presentStr[0] not in ('-', '0'):
            self.num.set('-' + presentStr)

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
        buttonCE = tkinter.Button(root, text='CE', bg='lightgray', command=self.clearAll)
        buttonCE.place(relx=0, rely=0.4, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        buttonCE.bind('<Enter>', self.changeBg)
        buttonCE.bind('<Leave>', self.backBg)

        buttonC = tkinter.Button(root, text='C', bg='lightgray', command=self.clearAll)
        buttonC.place(relx=0.25, rely=0.4, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        buttonC.bind('<Enter>', self.changeBg)
        buttonC.bind('<Leave>', self.backBg)

        buttonDel = tkinter.Button(root, text='<-', bg='lightgray', command=self.backSpace)
        buttonDel.place(relx=0.5, rely=0.4, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        buttonDel.bind('<Enter>', self.changeBg)
        buttonDel.bind('<Leave>', self.backBg)

        buttonDiv = tkinter.Button(root, text='÷', bg='lightgray', command=lambda: self.operation('/'))
        buttonDiv.place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        buttonDiv.bind('<Enter>', self.changeBg)
        buttonDiv.bind('<Leave>', self.backBg)

        button1 = tkinter.Button(root, text='1', bg='lightgray', command=lambda: self.buttonAction('1'))
        button1.place(relx=0, rely=0.5, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button1.bind('<Enter>', self.changeBg)
        button1.bind('<Leave>', self.backBg)

        button2 = tkinter.Button(root, text='2', bg='lightgray', command=lambda: self.buttonAction('2'))
        button2.place(relx=0.25, rely=0.5, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button2.bind('<Enter>', self.changeBg)
        button2.bind('<Leave>', self.backBg)

        button3 = tkinter.Button(root, text='3', bg='lightgray', command=lambda: self.buttonAction('3'))
        button3.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button3.bind('<Enter>', self.changeBg)
        button3.bind('<Leave>', self.backBg)

        buttonX = tkinter.Button(root, text='x', bg='lightgray', command=lambda: self.operation('*'))
        buttonX.place(relx=0.75, rely=0.5, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        buttonX.bind('<Enter>', self.changeBg)
        buttonX.bind('<Leave>', self.backBg)

        button4 = tkinter.Button(root, text='4', bg='lightgray', command=lambda: self.buttonAction('4'))
        button4.place(relx=0, rely=0.6, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button4.bind('<Enter>', self.changeBg)
        button4.bind('<Leave>', self.backBg)

        button5 = tkinter.Button(root, text='5', bg='lightgray', command=lambda: self.buttonAction('5'))
        button5.place(relx=0.25, rely=0.6, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button5.bind('<Enter>', self.changeBg)
        button5.bind('<Leave>', self.backBg)

        button6 = tkinter.Button(root, text='6', bg='lightgray', command=lambda: self.buttonAction('6'))
        button6.place(relx=0.5, rely=0.6, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button6.bind('<Enter>', self.changeBg)
        button6.bind('<Leave>', self.backBg)

        button_ = tkinter.Button(root, text='-', bg='lightgray', command=lambda: self.operation('-'))
        button_.place(relx=0.75, rely=0.6, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button_.bind('<Enter>', self.changeBg)
        button_.bind('<Leave>', self.backBg)

        button7 = tkinter.Button(root, text='7', bg='lightgray', command=lambda: self.buttonAction('7'))
        button7.place(relx=0, rely=0.7, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button7.bind('<Enter>', self.changeBg)
        button7.bind('<Leave>', self.backBg)

        button8 = tkinter.Button(root, text='8', bg='lightgray', command=lambda: self.buttonAction('8'))
        button8.place(relx=0.25, rely=0.7, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button8.bind('<Enter>', self.changeBg)
        button8.bind('<Leave>', self.backBg)

        button9 = tkinter.Button(root, text='9', bg='lightgray', command=lambda: self.buttonAction('9'))
        button9.place(relx=0.5, rely=0.7, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button9.bind('<Enter>', self.changeBg)
        button9.bind('<Leave>', self.backBg)

        buttonAdd = tkinter.Button(root, text='+', bg='lightgray', command=lambda: self.operation('+'))
        buttonAdd.place(relx=0.75, rely=0.7, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        buttonAdd.bind('<Enter>', self.changeBg)
        buttonAdd.bind('<Leave>', self.backBg)

        buttonFlag = tkinter.Button(root, text='±', bg='lightgray', command=self.pm)
        buttonFlag.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        buttonFlag.bind('<Enter>', self.changeBg)
        buttonFlag.bind('<Leave>', self.backBg)

        button0 = tkinter.Button(root, text='0', bg='lightgray', command=lambda: self.buttonAction('0'))
        button0.place(relx=0.25, rely=0.8, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        button0.bind('<Enter>', self.changeBg)
        button0.bind('<Leave>', self.backBg)

        buttonPoint = tkinter.Button(root, text='.', bg='lightgray', command=lambda: self.buttonAction('.'))
        buttonPoint.place(relx=0.5, rely=0.8, relwidth=0.25, relheight=0.1)
        # 绑定按钮 生成鼠标经过变色效果
        buttonPoint.bind('<Enter>', self.changeBg)
        buttonPoint.bind('<Leave>', self.backBg)

        buttonEque = tkinter.Button(root, text='=', bg='lightgray', command=self.getResult)
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