# 决策树
# 非参数的学习算法
# 可以解决分类问题，天然可以解决多分类问题
# 也可以解决回归问题
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()
print(iris.data)
x = iris.data[:,2:]
y = iris.target
print(y==2)
# plt.scatter(x[y==0,0],x[y==0,1])
# plt.scatter(x[y==1,0],x[y==1,1])
# plt.scatter(x[y==2,0],x[y==2,1])
# plt.show()

from sklearn.tree import DecisionTreeClassifier
dt_clf = DecisionTreeClassifier(max_depth=2,criterion='entropy')
dt_clf.fit(x,y)

def plot_decision_boundary(model,axis):
    x0,x1=np.meshgrid(
        np.linspace(axis[0],axis[1],int((axis[1])-axis[0])*100).reshape(-1,1),
        np.linspace(axis[2],axis[3],int((axis[3])-axis[2])*100).reshape(-1,1)
    )
    x_new = np.c_[x0.ravel(),x1.ravel()]

    y_predict = model.predict(x_new)
    zz = y_predict.reshape(x0.shape)

    from matplotlib.colors import  ListedColormap
    custom_cmap = ListedColormap(['#EF9A9A','#FFF59D','#90CAF9'])

    plt.contourf(x0,x1,zz,cmap=custom_cmap)

plot_decision_boundary(dt_clf,axis=[0,8,0,3])

plt.scatter(x[y==0,0],x[y==0,1])
plt.scatter(x[y==1,0],x[y==1,1])
plt.scatter(x[y==2,0],x[y==2,1])
plt.show()

# 怎么在每个节点在哪个维度做划分
# 某个维度在哪个值上做划分
# 划分后使得信息熵降低

# 模拟使用信息熵进行划分
def split(x,y,d,value):  # 维度d  阈值value
    index_a = (x[:,d]<=value)
    index_b = ()

# 基尼系数对决策树的划分
iris = datasets.load_iris()
print(iris.data)
x = iris.data[:,2:]
y = iris.target
print(y==2)
plt.scatter(x[y==0,0],x[y==0,1])
plt.scatter(x[y==1,0],x[y==1,1])
plt.scatter(x[y==2,0],x[y==2,1])
plt.show()

from sklearn.tree import DecisionTreeClassifier
dt_clf = DecisionTreeClassifier(max_depth=2,criterion='gini')
dt_clf.fit(x,y)

