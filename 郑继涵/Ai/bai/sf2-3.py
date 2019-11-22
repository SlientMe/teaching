# 波士顿房产数据
# 多元线性回归
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

boston = datasets.load_boston()
x = boston.data
y = boston.target
x = x[y<50.0]
y = y[y<50.0]

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=666)
lin_reg = LinearRegression()
lin_reg.fit(x_train,y_train)
print(lin_reg.coef_) # 得到的系数矩阵
print(lin_reg.intercept_) # 截距
print(lin_reg.score(x_test,y_test)) # 评分

# KNN的可解释性
# 对系数矩阵排序
coef = lin_reg.coef_  # 有正有负，正相关，负相关
argcoef = np.argsort(coef)  # 这里是对索引排序
print(boston.feature_names) # 这里就是对房价影响的因素
print(boston.feature_names[argcoef])  # 这里就是对房价因素影响的排序结果
print(boston.DESCR)


# 使用 KNN解决回归问题
from sklearn.neighbors import KNeighborsRegressor

knn_reg = KNeighborsRegressor() # k默认为5
knn_reg.fit(x_train,y_train)
print(knn_reg.predict(x_test))
print(knn_reg.score(x_test,y_test))

# 使用网格搜索对knn的超参数来最优
from sklearn.model_selection import GridSearchCV
param_grid = [
    {
        "weights":['uniform'],
        'n_neighbors':[i for i in range(1,11)]
    },{
        "weights":['distance'],
        'n_neighbors':[i for i in range(1,11)],
        'p':[i for i in range(1,6)]
    }
]
knn_reg1 = KNeighborsRegressor()
grid_search = GridSearchCV(knn_reg1,param_grid,n_jobs=-1)
grid_search.fit(x_train,y_train)
print(grid_search.best_params_)
print(grid_search.best_score_) # 这里CV是使用了交差验证，和上面的不一样，所以不能评价
print(grid_search.best_estimator_.score(x_test,y_test))  # 这才是和上面score相同的评价标准
