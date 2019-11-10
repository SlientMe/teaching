# 读取数据和简单的数据探索
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()  # 可以看成字典
print(iris.keys())
print(iris.data)  # 拿到数据
print(iris.data.shape)

x = iris.data[:,:2]  # 只能绘制2维图像，所以只要前两列
plt.scatter(x[:,0],x[:,1])
plt.show()



