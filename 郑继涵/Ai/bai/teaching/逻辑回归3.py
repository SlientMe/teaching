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

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=666)
print(x_train)
print(y_train)
# 使用sklearn使用简单线性逻辑回归
log_reg = LogisticRegression()
log_reg.fit(x_train,y_train)
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
plot_decision_boundary(log_reg,axis=[-3,3,-3,3])

plt.scatter(x[y==0,0],x[y==0,1])
plt.scatter(x[y==1,0],x[y==1,1])
# plt.scatter(x,x)
plt.show()

print(log_reg.score(x_train,y_train)) # 简单的线性回归，正确率不是很高
print(log_reg.score(x_test,y_test))

# https://www.cnblogs.com/volcao/p/9385930.html
# 使用sklearn使用多项式逻辑回归
# 使用管道:Pipeline(list)，list 内的每一个元素为为管道的一步，每一步是一个元组，
        # 元组的第一个元素是一个字符串，是一个实例对象，描述这一步的内容或功能，第二个元素是一个类的对象

def PolynomialLogisticRegression(degree):
    return Pipeline([
        # 管道第一步：给样本特征添加多形式项；
        ('poly',PolynomialFeatures(degree=degree)),
        # 管道第二步：数据归一化处理；
        ('std_scaler',StandardScaler()),
        ('log_reg',LogisticRegression())
    ])
poly_log_reg = PolynomialLogisticRegression(degree=6)
poly_log_reg.fit(x_train,y_train)

plot_decision_boundary(poly_log_reg,axis=[-3,3,-3,3])
plt.scatter(x[y==0,0],x[y==0,1])
plt.scatter(x[y==1,0],x[y==1,1])
# plt.scatter(x,x)
plt.show()
print(poly_log_reg.score(x_train,y_train))
print(poly_log_reg.score(x_test,y_test))