# https://blog.csdn.net/jk123vip/article/details/80591619
# https://blog.csdn.net/juwikuang/article/details/90319273
# https://www.cnblogs.com/lliuye/p/9129493.html

#   我们可以按照任务的种类,将任务分为回归任务和分类任务.那这两者的区别是什么呢?
#   按照较官方些的说法,  输入变量与输出变量均为连续变量的预测问题是回归问题,
#   输出变量为有限个离散变量的预测问题成为分类问题. 通俗一点讲,我们要预测的结果
#   是一个数,比如要通过一个人的饮食预测一个人的体重,体重的值可以有无限多个,#
#   有的人50kg,有的人51kg,在50和51之间也有无限多个数.这种预测结果是某一个确定数,
#   而具体是哪个数有无限多种可能的问题,# 我们会训练出一个模型,传入参数后得到这
#   个确定的数,这类问题我们称为回归问题.预测的这个变量(体重)因为有无限多种可能
# ,在数轴上是连续的,所以我们称这种变量为连续变量.#  我们要预测一个人身
#  体健康或者不健康,预测会得癌症或者不会得癌症,预测他是水瓶座,
# 天蝎座还是射手座,这种结果只有几个值或者多个值的问题,我们可以把每个值都当做一类,
# 预测对象到底属于哪一类.这样的问题称为分类问题.如果一个分类问题的结果只有两个,
# 比如"是"和"不是"两个结果,我们把结果为"是"的样例数据称为"正例",讲结果为
# "不是"的样例数据称为"负例",对应的,这种结果的变量称为离散型变量.


# 线性回归完成的是回归拟合任务，而对于分类任务，我们同样需要一条线，
# 但不是去拟合每个数据点，而是把不同类别的样本区分开来。

# 预测函数
# 对于二分类问题，y∈{0,1}y∈{0,1}，1表示正例，0表示负例。
# 逻辑回归是在线性函数θTxθTx输出预测实际值的基础上，寻找一个假设函数函数hθ(x)=g(θTx)hθ(x)=g(θTx)，
# 将实际值映射到到0，1之间，如果hθ(x)>=0.5hθ(x)>=0.5，则预测y=1y=1，及yy属于正例；如果hθ(x)<0.5hθ(x)<0.5，则预测y=0y=0，即yy属于负例。

# 逻辑回归中选择对数几率函数（logistic function）作为激活函数，对数几率函数是Sigmoid函数（形状为S的函数）的重要代表

# 非线性逻辑回归的代码实现（sklearn）
# https://blog.csdn.net/qq_30377909/article/details/90949866

from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

x_data,y_data = datasets.make_gaussian_quantiles(n_samples=500,n_features=2,n_classes=2,random_state=666)


# print(y_data)
# plt.scatter(x_data[:,0],x_data[:,1],c=y_data)
# plt.scatter(x_data[:,1],y_data)
# plt.show()

logistic = LogisticRegression(solver='liblinear')
logistic.fit(x_data, y_data)
# 观察未定义多项式回归时会如何分类

# 获取数据值所在的范围
x_min, x_max = x_data[:, 0].min() - 1, x_data[:, 0].max() + 1
y_min, y_max = x_data[:, 1].min() - 1, x_data[:, 1].max() + 1

# 生成网格矩阵
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                    np.arange(y_min, y_max, 0.02))

z = logistic.predict(np.c_[xx.ravel(), yy.ravel()])
z = z.reshape(xx.shape)
#等高线图
cs = plt.contourf(xx, yy, z)
#样本散点图
plt.scatter(x_data[:, 0], x_data[:, 1], c=y_data)

plt.show()
print('score:', logistic.score(x_data, y_data))


# 接下来定义多项式回归

#定义多项式回归,degree的值可以调节多项式的特征
poly_reg = PolynomialFeatures(degree=5)
#特征处理
x_poly = poly_reg.fit_transform(x_data)
#定义逻辑回归模型
logistic = LogisticRegression(solver='liblinear')
#训练模型
logistic.fit(x_poly, y_data)
#获取数据值所在的范围
x_min, x_max = x_data[:, 0].min() - 1, x_data[:, 0].max() + 1
y_min, y_max = x_data[:, 1].min() - 1, x_data[:, 1].max() + 1

#生成网格矩阵
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                    np.arange(y_min, y_max, 0.02))

z = logistic.predict(poly_reg.fit_transform(np.c_[xx.ravel(), yy.ravel()]))
z = z.reshape(xx.shape)
#等高线图
cs = plt.contourf(xx, yy, z)
#样本散点图
plt.scatter(x_data[:, 0], x_data[:, 1], c=y_data)
plt.show()

print('score', logistic.score(x_poly, y_data))
