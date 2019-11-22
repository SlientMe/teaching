# 支撑向量机SVM（support vector machine）
# 解决分类和 回归  其实就是最大化margin
# scikit-learn中的SVM
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

x = iris.data
y = iris.target

x = x[y<2,:2]
y = y[y<2]

plt.scatter(x[y==0,0],x[y==0,1],color = 'red')
plt.scatter(x[y==1,0],x[y==1,1],color="blue")
plt.show()