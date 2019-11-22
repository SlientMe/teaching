# 波士顿房产数据
# 多元线性回归
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

boston = datasets.load_boston()
x,y = boston.data,boston.target
# 1.3对数据进行正规化处理

#进行数据预处理
# https://www.jianshu.com/p/59d4a7727f37
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
#将数据归化到正态分布，均值为0,方差为1
bostonDf_X = pd.DataFrame(boston.data,columns=boston.feature_names)
bostonDf_y = pd.DataFrame(boston.target,columns=['houseprice'])#注意加列名称
#合并dataframe
bostonDf = pd.concat([bostonDf_X,bostonDf_y],axis=1)#axis=1为横向操作

bostonStd = scaler.fit_transform(bostonDf.values)
standarx = pd.DataFrame(bostonStd,columns=bostonDf.columns)
print(standarx.head(10))

# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=666)
x_train,x_test,y_train,y_test = train_test_split(bostonStd[:,0:13],bostonStd[:,13],test_size=0.3,random_state=0)

lg = LinearRegression()
lg.fit(x_train,y_train)
print(lg.coef_)  # 打印回归系数
print(lg.intercept_)  # 打印截距项
y_train_predict = lg.predict(x_train)
print(lg.score(x_train,y_train))



