import math
import xlrd
from pyecharts.charts import Scatter3D,Page
import random

alldata = []   # 所有坐标点
verList = []   # 垂直点
horList = []   # 水平点
firstPoint = [0,50000,5000]  # 起始点
verden = []
horden = []

def excel_to_matrix(path):
    table = xlrd.open_workbook(path).sheets()[0]  # 获取第一个sheet表
    row = table.nrows  # 行数
    col = table.ncols  # 列数
    for x in range(row):
        cols = table.row_values(x)  # 把list转换为矩阵进行矩阵操作
        alldata.append(cols)
    for d in alldata:
        if d[4]==1:
            verList.append(d)
        elif d[4]==0:
            horList.append(d)

datafile = 'data1.xlsx'
excel_to_matrix(datafile)

def calc_pointTopoint(point1,poin2):
    dentence = 0
    for i in range(3):
        dentence += (point1[i]-poin2[i])**2
    dentence = math.sqrt(dentence)
    return dentence

def calc_pointToline(point):
    k = (100000*point[0]-9652.34*(point[1]-50000)-22*(point[2]-5000))/(100000**2+9652.34**2+22**2)
    x = k*100000
    y = -9652.34*k+50000
    z = -22*k+5000
    verpoint = [x,y,z]
    return calc_pointTopoint(point,verpoint)


def checkhor(point):  # 检测水平方向
    meetPoint = []
    d = []
    for i in horList:
        i = i[1:4]
        d1 = calc_pointTopoint(point,i)
        if d1<20/0.001:
            d2 = calc_pointToline(i)
            meetPoint.append(d2/d1)
            d.append(d1)
    horden.append(d[meetPoint.index(min(meetPoint))])
    return horList[meetPoint.index(min(meetPoint))]

def checkver(point):  # 检测垂直方向
    meetPoint = []
    d = []
    for i in verList:
        i = i[1:4]
        d3 = calc_pointTopoint(point,i)
        if d3<15/0.001:
            d4 = calc_pointToline(i)
            meetPoint.append(d4/d3)
            d.append(d3)
    verden.append(d[meetPoint.index(min(meetPoint))])
    return verList[meetPoint.index(min(meetPoint))]

tracelist = []
nextpoint = []
for k in range(len(alldata)):
    if k == 0:
        nextpoint = checkhor(firstPoint)[1:4]
    elif k%2==0:
        nextpoint = checkhor(nextpoint)[1:4]
    elif k%2==1:
        nextpoint = checkver(nextpoint)[1:4]
    tracelist.append(nextpoint)

# print(horden)
# print(verden)
print(len(tracelist))
print(tracelist)

page = Page()# st
# data = [[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)] for _ in range(80)]
data = tracelist
# for d in alldata:
#     temp = d[1:4]
#     temp.append(d[0])
#     print(temp)
#     data.append(temp)
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
scatter3D = Scatter3D() #设置图表的高和宽
scatter3D.add("", data,True, range_color) #视觉映射和颜色选择
page.add(scatter3D)
page.render()