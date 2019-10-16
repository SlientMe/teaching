''''
Text窗口部件
　　简单说明：Text是tkinter类中提供的的一个多行文本区域，显示多行文本，可用来收集(或显示)用户输入的文字(类似 HTML 中的 textarea)，
格式化文本显示，允许你用不同的样式和属性来显示和编辑文本，同时支持内嵌图象和窗口。
'''
import tkinter as tk  # 使用Tkinter前需要先导入
# 第1步，实例化object，建立窗口window
window = tk.Tk()
# 第2步，给窗口的可视化起名字
window.title('My Window')
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
# 第4步，在图形界面上设定输入框控件entry框并放置
e = tk.Entry(window, show=None)  # 显示成明文形式
e.pack()

# 第5步，定义两个触发事件时的函数insert_point和insert_end（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）
def insert_point():  # 在鼠标焦点处插入输入内容
    var = e.get()
    t.insert('insert', var)

def insert_end():  # 在文本框内容最后接着插入输入内容
    var = e.get()
    t.insert('end', var)

# 第6步，创建并放置两个按钮分别触发两种情况
b1 = tk.Button(window, text='insert point', width=10,height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end', width=10,height=2, command=insert_end)
b2.pack()

# 第7步，创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度
t = tk.Text(window, height=3)
t.pack()

# 第8步，主窗口循环显示
window.mainloop()


'''
Lambda函数又称为匿名函数
Lambda函数的优点很明显，通过一行代码就定义了一个函数，有效减少了代码的行数，而且省去了定义函数名的烦恼，降低了函数名冲突的风险。
当然lambda函数也存在缺点，由于它只能表示为一行代码，因此不能使用多分支判断、for循环、异常处理等复杂逻辑。

  lambda x, y: x*y；函数输入是x和y，输出是它们的积x*y
     lambda:None；函数没有输入参数，输出是None
     lambda *args: sum(args); 输入是任意个数的参数，输出是它们的和(隐性要求是输入参数必须能够进行加法运算)
     lambda **kwargs: 1；输入是任意键值对参数，输出是1
————————————————


func = lambda x,y : x+y
print(func(1,2))
#等同与普通函数
def sum(x,y):
    return x+y
print(sum(1,2))

1.将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数。

例如，执行语句add=lambda x, y: x+y，定义了加法函数lambda x, y: x+y，并将其赋值给变量add，这样变量add便成为具有加法功能的函数。例如，执行add(1,2)，输出为3。
————————————————



'''