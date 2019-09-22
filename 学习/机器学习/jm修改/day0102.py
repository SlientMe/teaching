import math
import xlrd
from pyecharts.charts import Scatter3D,Page
import random

alldata = []   # 所有坐标点
verList = []   # 垂直点
horList = []   # 水平点
firstPoint = [0,50000,5000]  # 起始点
endPoint = [100000,74860.54,5499.61]  #终止点
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

datafile = 'data2.xlsx'
excel_to_matrix(datafile)

def calc_pointTopoint(point1,poin2):
    dentence = 0
    for i in range(3):
        dentence += (point1[i]-poin2[i])**2
    dentence = math.sqrt(dentence)
    return dentence


def checkhor(point,l):  # 检测水平方向
    meet = {}
    for i in horList:
        d1 = calc_pointTopoint(point,i[1:4])
        if d1<15/0.001 and d1<15/0.001-l:
            d2 = calc_pointTopoint(i[1:4],endPoint)
            meet[d2/d1]=[i,d1]
    return meet


def checkver(point,l):  # 检测垂直方向
    meet = {}
    for i in verList:
        d3 = calc_pointTopoint(point,i[1:4])
        if d3<10/0.001 and d3<20/0.001-l:
            d4 = calc_pointTopoint(i[1:4],endPoint)
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
        print(houxuan)
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
                tracelist.append(nextpoint)
                horden.append(truenextdent)
                print("0tracelist+++++++%s"%tracelist)
                m += 1
                break
    elif m%2 == 1: # 垂直
        houxuan = checkver(nextpoint, truenextdent)
        tempkey = []
        for i in houxuan:
            tempkey.append(i)
        tempkey.sort()
        print("11111111111")
        for j in tempkey:
            tempnextpoint = houxuan[j][0][1:4]
            tempnextdent = houxuan[j][1]
            if len(checkhor(tempnextpoint, tempnextdent)) > 0:
                nextpoint = tempnextpoint
                truenextdent = tempnextdent
                tracelist.append(nextpoint)
                verden.append(truenextdent)
                print("111111111tracelist+++++++%s"%tracelist)

                m += 1
                break
    elif m%2 == 0: # 水平
        houxuan = checkhor(nextpoint,truenextdent)
        tempkey = []
        for i in houxuan:
            tempkey.append(i)
        tempkey.sort()
        print("22222222222")
        for j in tempkey:
            tempnextpoint = houxuan[j][0][1:4]
            tempnextdent = houxuan[j][1]
            if len(checkver(tempnextpoint, tempnextdent)) > 0:
                nextpoint = tempnextpoint
                truenextdent = tempnextdent
                tracelist.append(nextpoint)
                horden.append(truenextdent)
                print("00000000000000tracelist+++++++%s"%tracelist)

                m += 1
                break
    if calc_pointTopoint(nextpoint,endPoint)<30/0.001:
        break
tracelist.insert(0,firstPoint)
tracelist.append(endPoint)
print(len(tracelist))
print(tracelist)




