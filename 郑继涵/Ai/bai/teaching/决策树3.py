# https://www.cnblogs.com/Yanjy-OnlyOne/p/11372286.html
#1-1导入基础训练数据集
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
d=datasets.load_iris()
x=d.data[:,2:]
y=d.target
print(x)
# plt.figure()
# plt.scatter(x[y==0,0],x[y==0,1],color="r")
# plt.scatter(x[y==1,0],x[y==1,1],color="g")
# plt.scatter(x[y==2,0],x[y==2,1],color="b")
# plt.show()

# 1-2导入sklearn 中的决策树算法进行数据的分类问题实现训练预测
from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier(max_depth=2,criterion="entropy")  # 定义决策树的分类器相关决策超参数
'''
max_depth: int型或None，可选(默认=None)树的最大深度，对于防止过拟合非常有用。如果不输入的话，
决策树在建立子树的时候不会限制子树的深度。一般来说，数据少或者特征少的时候可以不管这个值。
如果模型样本量多，特征也多的情况下，推荐限制这个最大深度，具体的取值取决于数据的分布。
常用的可以取值10-100之间。
'''
# DecisionTreeRegressor
dt.fit(x,y)
def plot_decision_boundary(model,axis):   # 决策边界输出函数（二维数据点）
    x0,x1=np.meshgrid(
        np.linspace(axis[0],axis[1],int((axis[1]-axis[0])*100)).reshape(-1,1),
        np.linspace(axis[2],axis[3], int((axis[3] - axis[2]) * 100)).reshape(-1,1)
    )
    x_new=np.c_[x0.ravel(),x1.ravel()]
    y_pre=model.predict(x_new)
    zz=y_pre.reshape(x0.shape)
    from matplotlib.colors import ListedColormap
    cus=ListedColormap(["#EF9A9A","#FFF59D","#90CAF9"])
    plt.contourf(x0,x1,zz,cmap=cus)

plot_decision_boundary(dt,axis=[0.5,8,0,3])
plt.scatter(x[y==0,0],x[y==0,1],color="r")
plt.scatter(x[y==1,0],x[y==1,1],color="g")
plt.scatter(x[y==2,0],x[y==2,1],color="b")

plt.show()