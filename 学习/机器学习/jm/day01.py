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
vererror = []
horden = []
horerror = []

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


def checkhor(point,l):  # 检测水平方向
    meetPoint = []
    meet = []
    d = []
    for i in horList:
        d1 = calc_pointTopoint(point,i[1:4])
        if d1<20/0.001 and d1<20/0.001-l:  # d5<20-d3  15   15
            d2 = calc_pointTopoint(i[1:4],endPoint)
            meetPoint.append(d2/d1)
            meet.append(i)
            d.append(d1)
    horden.append(d[meetPoint.index(min(meetPoint))])
    print("水平误差减去后的值%s"%(d[meetPoint.index(min(meetPoint))]+l))
    print("水平误差减%s"%d[meetPoint.index(min(meetPoint))])
    return meet[meetPoint.index(min(meetPoint))]


def checkver(point,l):  # 检测垂直方向
    meetPoint = []
    meet = []
    d = []
    for i in verList:
        d3 = calc_pointTopoint(point,i[1:4])
        if d3<15/0.001 and d3<25/0.001-l:  # d3<=25-d1   10  20
            d4 = calc_pointTopoint(i[1:4],endPoint)
            meetPoint.append(d4/d3)
            meet.append(i)
            d.append(d3)

    verden.append(d[meetPoint.index(min(meetPoint))])
    print("垂直误差减去后的值%s"%(d[meetPoint.index(min(meetPoint))]+l))
    print("垂直误差%s"%d[meetPoint.index(min(meetPoint))])
    return meet[meetPoint.index(min(meetPoint))]



tracelist = []
nextpoint = firstPoint
m = 0
n = 0
for k in range(len(alldata)):
    if k == 0:
        temp = checkhor(firstPoint,0)
        nextpoint = temp[1:4]
        tracelist.append(temp)
    elif k%2==0:
        temp = checkhor(nextpoint,verden[m])
        m += 1
        nextpoint = temp[1:4]
        tracelist.append(temp)
    elif k%2==1:
        temp = checkver(nextpoint,horden[n])
        n += 1
        nextpoint = temp[1:4]
        tracelist.append(temp)
    if calc_pointTopoint(nextpoint,endPoint)<20/0.001:
        break


newtracelist = []
for i in range(len(tracelist)):
    tracelistthree = tracelist[i][1:4]
    if tracelistthree not in newtracelist:
        newtracelist.append(tracelistthree)

for j in range(len(newtracelist)):
    for i in range(len(tracelist)):
        if newtracelist[j][0]==tracelist[i][1] and newtracelist[j][1]==tracelist[i][2] and newtracelist[j][2]==tracelist[i][3]:
            newtracelist[j].append(tracelist[i][0])
            break


verden = list(set(verden))
horden = list(set(horden))
newtracelist.insert(0,firstPoint)
newtracelist.append(endPoint)

print(len(newtracelist))
print(newtracelist)
print(horden)
print(verden)

print(newtracelist)
page = Page()# st
data = newtracelist
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
scatter3D = Scatter3D() #设置图表的高和宽
scatter3D.add("", data,True, range_color) #视觉映射和颜色选择
page.add(scatter3D)
page.render()