import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# 直线
# x = np.array([1, 2, 3])
# plt.plot(x)
# plt.show()

# 两条平行线
# x = np.array([1, 2, 3])
# y = np.array([5, 6, 7])
# plt.plot(x, label='first line')
# plt.plot(y, label='second line')
# # 横坐标注释
# plt.xlabel('Plot Number')
# # 列坐标注释
# plt.ylabel('Important var')
# # 生成表标题
# plt.title('Matplotlib demo\nCheck it out')
# # 生成小方块显示每条线对应的label
# plt.legend()
# plt.show()

#条形图
# one = np.array([[1, 3, 5, 7, 9], [3, 4, 6, 12, 7]])  前面是x的坐标，后面是y的坐标
# two = np.array([[2, 4, 6, 8, 10], [4, 2, 9, 8, 11]])
# # 参数1是横坐标，参数2是高度
# plt.bar(one[0], one[1], label='first')
# plt.bar(two[0], two[1], label='second')
# plt.xlabel('bar-hist Number')
# # 列坐标注释
# plt.ylabel('bar-hist height')
# # 生成表标题
# plt.title('Matplotlib demo\nCheck it out')
# # 生成小方块显示每条线对应的label
# plt.legend()
# plt.show()


#饼图
# slices = [7, 2, 5, 11]
# activities = ['sleeping', 'eating', 'working', 'playing']
# cols = ['c', 'm', 'r', 'b']
# # slices是切片比例，startangle是起始角度，explode可以拿出不是0的切片
# plt.pie(slices,
#         labels=activities,
#         colors=cols,
#         startangle=90,
#         shadow=True,
#         explode=(0, 0.1, 0, 0),
#         autopct='%1.1f%%')
# plt.title('Matplotlib demo\nCheck it out')
# plt.show()

# 文件中加载数据
# """
# test1.txt 内容格式如下
# 0   0
# 1  1
# 2  12
# 3  11
# 4  15
# 5  18
# 6  9
# 7  5
# 8  2
# 9  16
# ...
# """
# data = np.loadtxt('../data/test1.txt', unpack=True)
# plt.plot(data[0], data[1], label='Loaded from local file')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Matplotlib demo\nCheck it out')
# plt.legend()
# plt.show()


data = np.loadtxt('data1.txt', unpack=True)
x = data[1]
y = data[2]
z = data[3]

# x = np.random.randint(0,10,size=100)
# y = np.random.randint(-20,20,size=100)
fig = plt.figure()
axe3d = Axes3D(fig)
axe3d.scatter(x,y,z,c='r')
plt.show()
