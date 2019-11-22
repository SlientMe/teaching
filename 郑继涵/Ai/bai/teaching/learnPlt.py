import numpy as np
from matplotlib import pyplot as plt
x = np.arange(1,11)
y =  2  * x +  5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
# plt.axis(0,15,0,15)
plt.plot(x,y,'o')
plt.plot(x,y,'-') # --  :
plt.show()

# 以下脚本使用 matplotlib 生成正弦波图。

# 计算正弦曲线上点的 x 和 y 坐标
x = np.arange(0, 3  * np.pi,  0.1)
y = np.sin(x)
plt.title("sine wave form")
# 使用 matplotlib 来绘制点
plt.plot(x, y)
plt.show()

##########################################################
# 线性回归
x = np.array([1,2,3,4,5])
y = np.array([1,3,2,3,5])
plt.scatter(x,y)
plt.axis([0,6,0,6])

x_mean = np.mean(x)
y_mean = np.mean(y)

num = 0.0
d = 0.0
# zip() 函数用于将可迭代的对象作为参数，
# 将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
print(x)
print(y)
for xi,yi in zip(x,y):
    num += (xi-x_mean)*(yi-y_mean)
    d += (xi-x_mean)**2
a = num/d
b = y_mean-a*x_mean
y_hat = a*x + b
print(x)
print(y_hat)
plt.plot(x,y_hat,color='r')
plt.show()

##########################################################

# numpy.save() numpy.save()文件将输入数组存储在具有npy扩展名的磁盘文件中。
a = np.array([1,2,3,4,5])
# np.save('outfile',a)
# b = np.load('outfile.npy')

# 画3D图形
from pyecharts.charts import Scatter3D,Page

page = Page()# st

data = [[0, 50000, 5000], [16612.2732018317, 46538.5665294772, 9942.56660161132, 303.0], [23842.0307851423, 47349.1128458602, 9532.73861023007, 199.0], [27810.0363906167, 57543.804355148, 5123.83998827498, 80.0], [39684.0766890104, 56894.4082461272, 6550.4738181871, 170.0], [45591.7751823415, 61669.8984619136, 6431.02660574361, 282.0], [58196.7743465736, 67621.5803410544, 5278.05561374484, 288.0], [57832.9433239156, 72289.4863993616, 8328.02923220129, 118.0], [66456.9282742664, 80969.1680946618, 4674.70229447453, 469.0], [69039.4642283864, 78513.8662373976, 2994.73596031709, 601.0], [72922.4909659759, 65748.7433586562, 1514.31491761549, 406.0], [71478.5204190364, 63324.4598224261, 6963.77157503262, 448.0], [83098.5041291567, 58184.9511978424, 4513.62421196539, 397.0], [100000, 59652.34, 5022]]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
scatter3D = Scatter3D() #设置图表的高和宽
scatter3D.add("", data,True, range_color) #视觉映射和颜色选择
page.add(scatter3D)
page.render()

print(np.linspace(1,50,30).reshape(10,3))
print(np.eye(5,4,3))