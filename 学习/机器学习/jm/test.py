import xlrd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

alldata = []
def excel_to_matrix(path):
    table = xlrd.open_workbook(path).sheets()[0]  # 获取第一个sheet表
    row = table.nrows  # 行数
    col = table.ncols  # 列数
    for x in range(row):
        cols = table.row_values(x)  # 把list转换为矩阵进行矩阵操作
        alldata.append(cols)
    # for d in alldata:
    #     if d[4]==1:
    #         verList.append(d)
    #     elif d[4]==0:
    #         horList.append(d)

datafile = 'data2.xlsx'
excel_to_matrix(datafile)


x = []
y = []
z = []
# data = [[0, 50000, 5000], [77111.4436985019, 53865.1451047564, 4887.54630795409, 163.0], [17780.0238454461, 52287.8820953331, 5425.18268066295, 114.0], [21630.9390706733, 43809.5726120181, 3993.8030786814, 31.0], [22946.4249044886, 50574.5300623865, 4727.06374622126, 188.0], [24641.0257452872, 41360.9259758434, 6177.15659923413, 137.0], [100000, 59652.34, 5022]]
zuobiao = [1,276,151,239,235,310,306,124,232,161,192,849,541,947,642,327]
# for i in alldata:
#     if i[0] in zuobiao:
#         x.append(i[1])
#         y.append(i[2])
#         z.append(i[3])
for i in zuobiao:
    for j in alldata:
        if i==j[0]:
            x.append(j[1])
            y.append(j[2])
            z.append(j[3])

print(x)
fig = plt.figure()
ax = Axes3D(fig)  # 创建3D图的2种方式，第一种通过Axes3D将图片从二维变成三维，第二种通过在add_subplot(111,projection='3d'）将子图坐标修改成三维
ax.plot(x,y,z,'bo--')  # 参数与二维折现图不同的在于多了一个Z轴的数据
plt.show()

# plt.xlim(xmax=100000,xmin=0)
# plt.ylim(ymax=100000,ymin=0)
# plt.plot(x,y,'ro')
# plt.show()
