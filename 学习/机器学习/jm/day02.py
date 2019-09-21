import math
import xlrd
from pyecharts.charts import Scatter3D,Page
import random

alldata = []   # 所有坐标点
verList = []   # 垂直点
horList = []   # 水平点
firstPoint = [0,50000,5000]  # 起始点
endPoint = [100000,59652.34,5022]  #终止点
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
    global horList
    meetPoint = []
    meetPointLength = []
    d = []
    for i in horList:
        d1 = calc_pointTopoint(point,i[1:4])
        if d1==0:
            print("hor is 0")
        elif d1<20/0.001:
            d2 = calc_pointTopoint(i[1:4],endPoint)
            meetPointLength.append(d2/d1)
            meetPoint.append(i)
            d.append(d1)
    if len(meetPointLength)>0:
        for k in horList:
            if calc_pointTopoint(meetPoint[meetPointLength.index(min(meetPointLength))],k)<15/0.001:
                horList.remove(k)
        horden.append(meetPoint[meetPointLength.index(min(meetPointLength))])
        return meetPoint[meetPointLength.index(min(meetPointLength))]
    else:
        return []

def checkver(point):  # 检测垂直方向
    global verList
    meetPoint = []
    meetPointLength = []
    d = []
    for i in verList:
        d3 = calc_pointTopoint(point,i[1:4])
        if d3==0:
            print("ver is 0")
        elif d3<15/0.001:
            d4 = calc_pointTopoint(i[1:4],endPoint)
            meetPointLength.append(d4/d3)
            meetPoint.append(i)
            d.append(d3)
    if len(meetPointLength)>0:
        for k in verList:
            if calc_pointTopoint(meetPoint[meetPointLength.index(min(meetPointLength))],k)<15/0.001:
                verList.remove(k)
        verden.append(meetPoint[meetPointLength.index(min(meetPointLength))])
        return meetPoint[meetPointLength.index(min(meetPointLength))]
    else:
        return []


tracelist = []
currentPoint = firstPoint
for k in range(len(alldata)):
    if k == 0:
        currentPoint = checkhor(firstPoint)[1:4]
        tracelist.append(currentPoint)
        print(k)
    elif k%2==0:
        print(len(horList))
        if len(checkhor(currentPoint))>0:
            # if calc_pointTopoint(currentPoint,endPoint)>=calc_pointTopoint(checkhor(currentPoint)[1:4],endPoint):
                print(k)
                currentPoint = checkhor(currentPoint)[1:4]
                print("stop")
                tracelist.append(currentPoint)
    elif k%2==1:
        print(len(verList))
        if len(checkver(currentPoint))>0:
            # if calc_pointTopoint(currentPoint,endPoint)>=calc_pointTopoint(checkver(currentPoint)[1:4],endPoint):
                print(k)
                currentPoint = checkver(currentPoint)[1:4]
                tracelist.append(currentPoint)
    print(currentPoint)

# for k in range(len(alldata)):
#     if k == 0:
#         nextpoint = checkhor(firstPoint)[1:4]
#         tracelist.append(nextpoint)
#     elif k%2==0:
#         nextpoint = checkhor(nextpoint)[1:4]
#         tracelist.append(nextpoint)
#     elif k%2==1:
#         nextpoint = checkver(nextpoint)[1:4]
#         tracelist.append(nextpoint)



page = Page()# st
data = [[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)] for _ in range(80)]
data = tracelist
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
scatter3D = Scatter3D() #设置图表的高和宽
scatter3D.add("", data,True, range_color) #视觉映射和颜色选择
page.add(scatter3D)
page.render()