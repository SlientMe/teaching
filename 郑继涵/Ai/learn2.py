# numpy.array 中的运算
import numpy as np
A = np.arange(4).reshape(2,2)
print(A)
# 逆矩阵
B = np.linalg.inv(A)
print(A.dot(B))

# 聚合运算
L = np.random.random(100)
print(np.sum(L))
print(np.min(L))
print(np.max(L))

X = np.arange(16).reshape(4,-1)
print(np.sum(X))
print(np.sum(X,axis=0))  # 计算每一列的和
print(np.sum(X,axis=1))  # 计算每一行的和

print(np.prod(X)) # 计算所有元素的乘积
print(np.mean(X))  # 平均值
print(np.median(X)) # 中位数
print(np.var(X))  # 方差
print(np.std(X)) # 标准差
T = np.random.normal(0,1,size=100000)
print(np.mean(T))
print(np.std(T))
