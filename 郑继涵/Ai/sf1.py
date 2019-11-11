# KNN  主要解决分类问题，也可以解决回归问题
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from  sklearn.neighbors import  KNeighborsClassifier

iris = datasets.load_iris()
X = iris.data
y = iris.target

shuffle_indexes = np.random.permutation(len(X))
test_ratio = 0.2
test_size = int(len(X)*test_ratio)

test_indexes = shuffle_indexes[:test_size]
train_indexes = shuffle_indexes[test_size:]

X_train = X[train_indexes]
y_train = y[train_indexes]

X_test = X[test_indexes]
y_test = y[test_indexes]


'''
KNN_classifier = KNeighborsClassifier(n_neighbors=6)
KNN_classifier.fit(X_train,y_train)
y_predict = KNN_classifier.predict(X_test)
print(y_predict)
print(y_test)
print(KNN_classifier.score(X_test,y_test))  # 不用预测出y_predict，可以直接得到预测准确率
print(sum(y_test==y_predict))

# 从sklearn中的train_test_split分开训练和测试数据集
# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=666)

# 判断准确度
from sklearn.metrics import accuracy_score
# print(accuracy_score(y_test,y_predict))

'''

# 怎么找到最好的k呢？ 也就是超参数
# 根据经验和相关领域的知识

best_score = 0.0
best_k = -1
for k in range(1,11):
    # 考不考距离 :欧拉距离  哈曼顿距离  明可夫斯基距离
    knn_clf = KNeighborsClassifier(n_neighbors=k,weights="distance") # 默认是uniform
    knn_clf.fit(X_train,y_train)
    score = knn_clf.score(X_test,y_test)
    if score>best_score:
        best_k = k
        best_score = score
print(best_k)
print(best_score)

# 同网格搜索的方式找到多个超参数的最佳值

param_grid=[
    {
        'weights':['uniform'],
        'n_neighbors':[i for i in range(1,11)]
    },
    {
        'weights':['distance'],
        'n_neighbors':[i for i in range(1,11)],
        'p':[i for i in range(1,6)]
    }
]

knn_clf = KNeighborsClassifier()
from  sklearn.model_selection import GridSearchCV
# n_jobs就是有几个核进行工作运算，-1就是使用所有的核,verbose就是在工作中有一些相应的输出
grid_servh = GridSearchCV(knn_clf,param_grid,n_jobs=-1,verbose=2)
grid_servh.fit(X_train,y_train)

print(grid_servh.best_estimator_)
print(grid_servh.best_score_)
print(grid_servh.best_params_)











