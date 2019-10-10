import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = []
y = []
z = []
data = [[0, 50000, 5000], [12712.8372282571, 53865.1451047564, 4887.54630795409, 163.0], [17780.0238454461, 52287.8820953331, 5425.18268066295, 114.0], [21630.9390706733, 43809.5726120181, 3993.8030786814, 31.0], [22946.4249044886, 50574.5300623865, 4727.06374622126, 188.0], [24641.0257452872, 41360.9259758434, 6177.15659923413, 137.0], [100000, 59652.34, 5022]]

for i in data:
    x.append(i[0])
    y.append(i[1])
    z.append(i[2])


fig = plt.figure()
ax = Axes3D(fig)  # 创建3D图的2种方式，第一种通过Axes3D将图片从二维变成三维，第二种通过在add_subplot(111,projection='3d'）将子图坐标修改成三维
ax.plot(x,y,z,'bo--')  # 参数与二维折现图不同的在于多了一个Z轴的数据
plt.show()

# plt.xlim(xmax=100000,xmin=0)
# plt.ylim(ymax=100000,ymin=0)
# plt.plot(x,y,'ro')
# plt.show()
