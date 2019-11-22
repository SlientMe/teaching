import numpy as np
from matplotlib import pylab as pl

#############################################
# 简单的线性回归
# 定义训练数据
x = np.array([1,3,2,1,3])
y = np.array([14,24,18,17,27])

# 回归方程求取函数
def fit(x,y):
    if len(x) != len(y):
        return
    numerator = 0.0
    denominator = 0.0
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    for i in range(len(x)):
        numerator += (x[i]-x_mean)*(y[i]-y_mean)
        denominator += np.square((x[i]-x_mean))
    print('numerator:',numerator,'denominator:',denominator)
    b0 = numerator/denominator
    b1 = y_mean - b0*x_mean
    return b0,b1

# 定义预测函数
def predit(x,b0,b1):
    return b0*x + b1

# 求取回归方程
b0,b1 = fit(x,y)
print('Line is:y = %2.0fx + %2.0f'%(b0,b1))

# 预测
x_test = np.array([0.5,1.5,2.5,3,4])
y_test = np.zeros((1,len(x_test)))
for i in range(len(x_test)):
    y_test[0][i] = predit(x_test[i],b0,b1)

# 绘制图像
xx = np.linspace(0, 5)
yy = b0*xx + b1
pl.plot(xx,yy,'k-')
pl.scatter(x,y,cmap=pl.cm.Paired)
pl.scatter(x_test,y_test[0],cmap=pl.cm.Paired)
pl.show()
##########################################################################

##########################################################################
# 多元线性回归
from sklearn import datasets,linear_model

# 定义训练数据
x = np.array([[100,4,9.3],[50,3,4.8],[100,4,8.9],
              [100,2,6.5],[50,2,4.2],[80,2,6.2],
              [75,3,7.4],[65,4,6],[90,3,7.6],[90,2,6.1]])
print(x)
X = x[:,:-1]
Y = x[:,-1]
print(X,Y)

# 训练数据
regr = linear_model.LinearRegression()
regr.fit(X,Y)
#  print(regr.score())
print('coefficients(b1,b2...):',regr.coef_)  # 模型的系数
print('intercept(b0):',regr.intercept_)  # 模型的截距

# 预测
x_test = np.array([[102,6],[100,4]])
y_test = regr.predict(x_test)
print(y_test)




