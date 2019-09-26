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


data = [[0, 50000, 5000], [16612.2732018317, 46538.5665294772, 9942.56660161132, 303.0], [23842.0307851423, 47349.1128458602, 9532.73861023007, 199.0], [27810.0363906167, 57543.804355148, 5123.83998827498, 80.0], [39684.0766890104, 56894.4082461272, 6550.4738181871, 170.0], [45591.7751823415, 61669.8984619136, 6431.02660574361, 282.0], [58196.7743465736, 67621.5803410544, 5278.05561374484, 288.0], [57832.9433239156, 72289.4863993616, 8328.02923220129, 118.0], [66456.9282742664, 80969.1680946618, 4674.70229447453, 469.0], [69039.4642283864, 78513.8662373976, 2994.73596031709, 601.0], [72922.4909659759, 65748.7433586562, 1514.31491761549, 406.0], [71478.5204190364, 63324.4598224261, 6963.77157503262, 448.0], [83098.5041291567, 58184.9511978424, 4513.62421196539, 397.0], [100000, 59652.34, 5022]]
two_dimen_data = []
for i in data:
    two_dimen_data.append(i[0:2])
print(two_dimen_data)





# def calc_pointTopoint(point1,poin2):
#     dentence = 0
#     for i in range(3):
#         dentence += (point1[i]-poin2[i])**2
#     dentence = math.sqrt(dentence)
#     return dentence
#
#
# def checkhor(point,l):  # 检测水平方向
#     meetPoint = []
#     meet = {}   # 满足条件所有点的 d2/d1:[horpoin,d1]
#     for i in horList:
#         d1 = calc_pointTopoint(point,i[1:4])
#         if d1<20/0.001 and d1<20/0.001-l:  # d5<20-d3  15   15
#             d2 = calc_pointTopoint(i[1:4],endPoint)
#             meetPoint.append(d2/d1)
#             meet[d2/d1]=[i,d1]
#     return meet
#
#
#
# def checkver(point,l):  # 检测垂直方向
#     meetPoint = []
#     meet = {}
#     for i in verList:
#         d3 = calc_pointTopoint(point,i[1:4])
#         if d3<15/0.001 and d3<25/0.001-l:  # d3<=25-d1   10  20
#             d4 = calc_pointTopoint(i[1:4],endPoint)
#             meetPoint.append(d4/d3)
#             meet[d4/d3]=[i,d3]
#     return meet
#
#
# tracelist = []
# nextpoint = firstPoint
# tempnextdent = 0
# truenextdent = 0
# m = 0
# while True:
#     if m==0:   # 水平
#         houxuan = checkhor(nextpoint,0)
#         tempkey = []
#         for i in houxuan:
#             tempkey.append(i)
#         tempkey.sort()
#         for j in tempkey:
#             tempnextpoint = houxuan[j][0][1:4]
#             tempnextdent = houxuan[j][1]
#             if len(checkver(tempnextpoint,tempnextdent))>0:
#                 nextpoint = tempnextpoint
#                 truenextdent = tempnextdent
#                 print(truenextdent)
#                 tracelist.append(nextpoint)
#                 horden.append(truenextdent)
#                 if houxuan[j][0][5] ==1:
#                     srateh = srateh +1
#                 m += 1
#                 break
#     elif m%2 == 1: # 垂直
#         houxuan = checkver(nextpoint, truenextdent)
#         tempkey = []
#         for i in houxuan:
#             tempkey.append(i)
#         tempkey.sort()
#         for j in tempkey:
#             tempnextpoint = houxuan[j][0][1:4]
#             tempnextdent = houxuan[j][1]
#             if len(checkhor(tempnextpoint, tempnextdent)) > 0:
#                 nextpoint = tempnextpoint
#                 truenextdent = tempnextdent
#                 print(truenextdent)
#
#                 tracelist.append(nextpoint)
#                 verden.append(truenextdent)
#                 if houxuan[j][0][5] ==1:
#                     sratev = sratev+ 1
#                 m += 1
#                 break
#     elif m%2 == 0: # 水平
#         houxuan = checkhor(nextpoint,truenextdent)
#         tempkey = []
#         for i in houxuan:
#             tempkey.append(i)
#         tempkey.sort()
#         for j in tempkey:
#             tempnextpoint = houxuan[j][0][1:4]
#             tempnextdent = houxuan[j][1]
#             if len(checkver(tempnextpoint, tempnextdent)) > 0:
#                 nextpoint = tempnextpoint
#                 truenextdent = tempnextdent
#                 print(truenextdent)
#
#                 tracelist.append(nextpoint)
#                 horden.append(truenextdent)
#                 if houxuan[j][0][5] ==1:
#                     srateh = srateh +1
#                 m += 1
#                 break
#     if calc_pointTopoint(nextpoint,endPoint)<20/0.001:
#         break
# tracelist.insert(0,firstPoint)
# tracelist.append(endPoint)
# print(len(tracelist))
# print(tracelist)
