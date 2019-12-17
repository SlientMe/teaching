# sklearn 库中导入 svm 模块
from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt
'''
https://yifdu.github.io/2018/11/21/机器机器学习（一）——SVM/
https://www.cnblogs.com/fydeblog/p/9440474.html
https://blog.csdn.net/liugan528/article/details/79448379
https://blog.csdn.net/b285795298/article/details/81977271

'''
# 定义三个点和标签
X = np.random.randint(1,10,size=(3,2))
y = np.array([0, 0, 1])
print(X)
# 定义分类器，clf 意为 classifier，是分类器的传统命名
clf = svm.SVC(kernel = 'linear')  # .SVC（）就是 SVM 的方程，参数 kernel 为线性核函数
# 训练分类器
clf.fit(X, y)  # 调用分类器的 fit 函数建立模型（即计算出划分超平面，且所有相关属性都保存在了分类器 cls 里）
# 打印分类器 clf 的一系列参数

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
plot_decision_boundary(clf,axis=[0,10,0,10])
print(X[y==0,0])
plt.scatter(X[y==0,0],X[y==0,1])
plt.scatter(X[y==1,0],X[y==1,1])
plt.show()

print (clf)
# 支持向量
print (clf.support_vectors_)
# 属于支持向量的点的 index
print (clf.support_)
# 在每一个类中有多少个点属于支持向量
print (clf.n_support_)
# 预测一个新的点
print (clf.predict([[2,0]]))