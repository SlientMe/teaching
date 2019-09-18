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
————————————————
Button(self.master, text='7', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=0,command=lambda: self.pressNum('7'))
中lambda: self.pressNum('7')是一个匿名函数，而不是单纯调用self.pressNum()，但最后得到的效果就是调用self.pressNum()的效果是一样的。
只不过如果command=self.pressNum('7')这样的形式的话，那么在创建按键时就会直接执行self.pressNum('7')，程序就会出问题。
————————————————

按钮
使用Button()创建各个按键，其参数：
参数	解释
text	指定按钮上显示的文本
font	按钮上文本的字体和大小
fg	按钮的前景色，即文本颜色
bg	按钮的背景色
bd	按钮的边框宽度
command	按钮消息的回调函数


'''