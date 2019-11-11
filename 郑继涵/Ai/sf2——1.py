# 波士顿房产数据
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

boston = datasets.load_boston()
print(boston.DESCR)
print(boston.feature_names)
x = boston.data[:,5] # 只使用房间数量这个特征
y = boston.target
x = x[y<50.0]
y = y[y<50.0]

plt.scatter(x,y)
plt.show()
x_train,x_test,y_train,y_test = train_test_split(x,y)
print(x_train.shape)

x_mean = np.mean(x_train)
y_mean = np.mean(y_train)

num = 0.0  # 分子
d = 0.0  # 分母
for x_i,y_i in zip(x_train,y_train):
    num += (x_i-x_mean)*(y_i-y_mean)
    d += (x_i-x_mean)**2
a = num/d
b = y_mean - a*x_mean

y_predict = a*x_train+b
print(y_predict.shape)
plt.scatter(x_train,y_train)
plt.plot(x_train,y_predict,color="red")
plt.show()

# MSE
y_predict_test = a*x_test+b
mse_test = np.sum((y_predict_test-y_test)**2)/len(y_test)
print(mse_test)
# RMSE
import math
rmse_test = math.sqrt(mse_test)
print(rmse_test)
# MAE
mae_test = np.sum(np.absolute(y_predict_test-y_test))/len(y_test)
print(mae_test)

# 通过自带的方式获取
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
print(mean_squared_error(y_test,y_predict_test))
print(mean_absolute_error(y_test,y_predict_test))

# R Square
from sklearn.metrics import r2_score
print(r2_score(y_test,y_predict_test))  # 越接近1，表示模型效果越好
