# 逻辑回归算法  使用最多的算法
# 其实解决的是分类问题，只可以解决二分类的问题。  将样本的特征和样本发生
# 的概率联系起来，概率就是一个数（预测事件发生的概率）
# 计算出事件的发生概率，大于0.5（莫个数）就是发生。
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

np.random.seed(666)
x = np.random.normal(0,1,size=(200,2))
y = np.array(x[:,0]**2+x[:,1]<1.5,dtype="int")
for _ in range(20):  # 为样本添加一些噪音
    y[np.random.randint(200)] = 1
plt.scatter(x[y==0,0],x[y==0,1])
plt.scatter(x[y==1,0],x[y==1,1])
# plt.scatter(x,x)
plt.show()
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=666)

# 使用sklearn使用简单线性逻辑回归
log_reg = LogisticRegression()
log_reg.fit(x_train,y_train)
print(log_reg.score(x_train,y_train)) # 简单的线性回归，正确率不是很高
print(log_reg.score(x_test,y_test))

# 使用sklearn使用多项式逻辑回归
def PolynomialLogisticRegression(degree):
    return Pipeline([
        ('poly',PolynomialFeatures(degree=degree)),
        ('std_scaler',StandardScaler()),
        ('log_reg',LogisticRegression())
    ])
poly_log_reg = PolynomialLogisticRegression(degree=2)
poly_log_reg.fit(x_train,y_train)
print(poly_log_reg.score(x_train,y_train))
print(poly_log_reg.score(x_test,y_test))