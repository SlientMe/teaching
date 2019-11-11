# 数据归一化
# 将所有的数据映射到同一尺度
# 最值归一化：把所有的数据映射到0-1之间（x-Xmin）/(Xmax-Xmin)
'''
均值方差归一化：数据没有明显的边界，有可能存在极端数据值,把所有数据归
一到均值为0方差为1的分布中.  (x-Xmean)/s  xmean均值  s方差
'''

import numpy as np
import matplotlib.pyplot as plt

# 最值归一化
x = np.random.randint(0,100,size=100)
print((x-np.min(x))/(np.max(x)-np.min(x)))

x = np.random.randint(0,100,(50,2))
x = np.array(x,dtype=float)
print(x[:10,:])
x[:,0] = (x[:,0]-np.min(x[:,0]))/(np.max(x[:,0])-np.min(x[:,0]))
x[:,1] = (x[:,1]-np.min(x[:,1]))/(np.max(x[:,1])-np.min(x[:,1]))
print(x)
plt.scatter(x[:,0],x[:,1])
plt.show()
print(np.mean(x[:,0]))  # 均值
print(np.std(x[:,0]))  # 方差


# 均值方差归一化
x2= np.random.randint(0,100,(50,2))
x2 = np.array(x2,dtype=float)
x2[:,0] = (x2[:,0]-np.mean(x2[:,0]))/np.std(x2[:,0])
x2[:,1] = (x2[:,1]-np.mean(x2[:,1]))/np.std(x2[:,1])
plt.scatter(x2[:,0],x2[:,1])
plt.show()

#  Scikit-learn中的Scaler
from sklearn import datasets
from sklearn.model_selection import train_test_split
from  sklearn.preprocessing import StandardScaler
from  sklearn.neighbors import KNeighborsClassifier
iris = datasets.load_iris()
x = iris.data
y= iris.target
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=666)
stander = StandardScaler()
stander.fit(x_train) # 现在stader就保持了x_train中的关键信息
print(stander.mean_)
print(stander.scale_)
x_train = stander.transform(x_train) # 其实stander.transform(x_train)没有改变xtrain
x_test_standard = stander.transform(x_test)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)
print(knn.score(x_test_standard,y_test))




