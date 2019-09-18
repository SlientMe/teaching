import numpy as np
import xlrd
import networkx as nx
import matplotlib.pyplot as plt


def excel_to_matrix(path):
    table = xlrd.open_workbook(path).sheets()[1]  # 获取第一个sheet表
    row = table.nrows  # 行数
    col = table.ncols  # 列数

    datamatrix = np.zeros((row, col))  # 生成一个nrows行ncols列，且元素均为0的初始矩阵
    for x in range(col):
        cols = np.matrix(table.col_values(x))  # 把list转换为矩阵进行矩阵操作
        datamatrix[:, x] = cols  # 按列把数据存进矩阵中
    return datamatrix


datafile = 'test.xls'
print(excel_to_matrix(datafile))

G = nx.Graph()
for i in range(len(excel_to_matrix(datafile))):
    for j in range(len(excel_to_matrix(datafile))):
        G.add_edge(i, j)
nx.draw(G)
plt.show()