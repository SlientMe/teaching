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
sratev = 1
srateh = 1

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


def checkhor(point,l):  # 检测水平方向
    meet = {}   # 满足条件所有点的 d2/d1:[horpoin,d1]
    for i in horList:
        d1 = calc_pointTopoint(point,i[1:4])
        if i[5]==0:
            if d1<20/0.001 and d1<20/0.001-l:  # d5<20-d3  15   15
                d2 = calc_pointTopoint(i[1:4],endPoint)
                meet[d2/d1]=[i,d1]
        else:
            if d1<20/0.001 and d1<20/0.001-l:  # d5<20-d3  15   15
                global srateh
                d1 = d1+1000*srateh
                d2 = calc_pointTopoint(i[1:4],endPoint)-1000*srateh
                meet[d2/d1]=[i,d1]
    # horden.append(d[meetPoint.index(min(meetPoint))])  # 后面再添加
    return meet



def checkver(point,l):  # 检测垂直方向
    meet = {}
    for i in verList:
        d3 = calc_pointTopoint(point,i[1:4])
        if i[5]==0:
            if d3<15/0.001 and d3<25/0.001-l:  # d3<=25-d1   10  20
                d4 = calc_pointTopoint(i[1:4],endPoint)
                meet[d4/d3]=[i,d3]
        else:
            if d3<15/0.001 and d3<25/0.001-l:  # d3<=25-d1   10  20
                global sratev
                d3 = d3+1000*sratev
                d4 = calc_pointTopoint(i[1:4],endPoint)-1000*sratev
                meet[d4/d3]=[i,d3]
    return meet


tracelist = []
nextpoint = firstPoint
tempnextdent = 0
truenextdent = 0
m = 0
while True:
    if m==0:   # 水平
        houxuan = checkhor(nextpoint,0)
        tempkey = []
        for i in houxuan:
            tempkey.append(i)
        tempkey.sort()
        for j in tempkey:
            tempnextpoint = houxuan[j][0][1:4]
            tempnextdent = houxuan[j][1]
            if len(checkver(tempnextpoint,tempnextdent))>0:
                nextpoint = tempnextpoint
                truenextdent = tempnextdent
                print(truenextdent)
                tracelist.append(nextpoint)
                horden.append(truenextdent)
                if houxuan[j][0][5] ==1:
                    srateh = srateh +1
                m += 1
                break
    elif m%2 == 1: # 垂直
        houxuan = checkver(nextpoint, truenextdent)
        tempkey = []
        for i in houxuan:
            tempkey.append(i)
        tempkey.sort()
        for j in tempkey:
            tempnextpoint = houxuan[j][0][1:4]
            tempnextdent = houxuan[j][1]
            if len(checkhor(tempnextpoint, tempnextdent)) > 0:
                nextpoint = tempnextpoint
                truenextdent = tempnextdent
                print(truenextdent)

                tracelist.append(nextpoint)
                verden.append(truenextdent)
                if houxuan[j][0][5] ==1:
                    sratev = sratev+ 1
                m += 1
                break
    elif m%2 == 0: # 水平
        houxuan = checkhor(nextpoint,truenextdent)
        tempkey = []
        for i in houxuan:
            tempkey.append(i)
        tempkey.sort()
        for j in tempkey:
            tempnextpoint = houxuan[j][0][1:4]
            tempnextdent = houxuan[j][1]
            if len(checkver(tempnextpoint, tempnextdent)) > 0:
                nextpoint = tempnextpoint
                truenextdent = tempnextdent
                print(truenextdent)

                tracelist.append(nextpoint)
                horden.append(truenextdent)
                if houxuan[j][0][5] ==1:
                    srateh = srateh +1
                m += 1
                break
    if calc_pointTopoint(nextpoint,endPoint)<20/0.001:
        break
tracelist.insert(0,firstPoint)
tracelist.append(endPoint)
print(len(tracelist))
print(tracelist)
