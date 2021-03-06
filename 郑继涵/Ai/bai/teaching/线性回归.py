import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets


# 加载数据
iris = datasets.load_iris()  # 可以看成字典
# # 先用key方法查看数据集
# print(boston.keys())
# #这里的data有13个维度，506个样本，target就是我们要预测的房价，接下来再查看feature_names
# print(boston.feature_names)
# print(boston.DESCR)
print(iris.keys())
print(iris.data)  # 拿到数据
print(iris.data.shape)
x = iris.data[:,:2]  # 只能绘制2维图像，所以只要前两列
plt.scatter(x[:,0],x[:,1])
plt.show()


# https://blog.csdn.net/jiaoyangdetian/article/details/89326342
# 线性回归算法  主要解决回归问题
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.,2.,3.,4.,5.])
y = np.array([1.,3.,2.,3.,5.])

plt.scatter(x,y)
plt.axis([0,6,0,6])
plt.show()
# a = ()/()   b= y-ax 具体公式可以网上找出
x_mean = np.mean(x)
y_mean = np.mean(y)

num = 0.0  # 分子
d = 0.0  # 分母
for x_i,y_i in zip(x,y):
    num += (x_i-x_mean)*(y_i-y_mean)
    d += (x_i-x_mean)**2
a = num/d
b = y_mean - a*x_mean

y_hat = a*x +b
plt.scatter(x,y)
plt.plot(x,y_hat,color="red")
plt.axis([0,6,0,6])
plt.show()

# sklearn实现简单线性回归

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 加载数据，波士顿房价
boston = datasets.load_boston()
x, y = boston.data, boston.target

# 划分训练集和检验集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=10010)

# 使用训练集训练模型
reg = LinearRegression()
reg.fit(x_train, y_train)

# 使用模型进行预测
y_predict = reg.predict(x_test)

# 计算模型的预测值与真实值之间的均方误差MSE
print(mean_squared_error(y_test, y_predict))


# 多元线性回归
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression

'''
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression
使用场景：一般来说，只要我们觉得数据有线性关系，LinearRegression类是我们的首先。如果发现拟合或者预测的不好，再考虑用其他的线性回归库。
'''
fig = plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
ax = Axes3D(fig)

# 构造X数据
X = np.random.randint(0, 7, (20, 2))
# 构造y数据， y = 1 * x_0 + 2 * x_1 + 3，后面打印参数会发现，是一致的
y = np.dot(X, np.array([1, 2])) + 3
# 绘制原始数据
ax.scatter(X[:, 0], X[:, 1], y, marker='o')

# 参数打印
reg = LinearRegression().fit(X, y)
print('分数：', reg.score(X, y))
print('参数：', reg.coef_)
print('截距：', reg.intercept_)

# 测试数据生成
test_x0 = np.linspace(0, 5, 10)
test_x1 = np.linspace(0, 5, 10)
test_X = np.array([test_x0, test_x1]).T

pred_y = reg.predict(test_X)
print('预测：', pred_y)

# 生成预测图形
ax.plot(test_X[:, 0], test_X[:, 1], pred_y, c='r')
plt.show()


