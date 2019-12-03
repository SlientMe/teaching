# sklearn 库中导入 svm 模块
from sklearn import svm

# 定义三个点和标签
X = [[2, 0], [1, 1], [2,3]]
y = [0, 0, 1]
# 定义分类器，clf 意为 classifier，是分类器的传统命名
clf = svm.SVC(kernel = 'linear')  # .SVC（）就是 SVM 的方程，参数 kernel 为线性核函数
# 训练分类器
clf.fit(X, y)  # 调用分类器的 fit 函数建立模型（即计算出划分超平面，且所有相关属性都保存在了分类器 cls 里）
# 打印分类器 clf 的一系列参数
print (clf)
# 支持向量
print (clf.support_vectors_)
# 属于支持向量的点的 index
print (clf.support_)
# 在每一个类中有多少个点属于支持向量
print (clf.n_support_)
# 预测一个新的点
print (clf.predict([[2,0]]))
