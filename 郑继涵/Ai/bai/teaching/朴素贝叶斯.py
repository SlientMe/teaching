# https://www.cnblogs.com/huangyc/p/9734956.html
# https://blog.csdn.net/zwqjoy/article/details/80914383
# https://www.cnblogs.com/geo-will/p/10468401.html
# https://blog.csdn.net/u013850277/article/details/83996358
# https://www.cnblogs.com/huangyc/p/9734956.html


# https://blog.csdn.net/Forlogen/article/details/85126210
from sklearn import datasets
iris = datasets.load_iris()
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf = clf.fit(iris.data, iris.target)
y_pred=clf.predict(iris.data)
print("高斯朴素贝叶斯，样本总数： %d 错误样本数 : %d" % (iris.data.shape[0],(iris.target != y_pred).sum()))
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf = clf.fit(iris.data, iris.target)
y_pred=clf.predict(iris.data)
print("多项分布朴素贝叶斯，样本总数： %d 错误样本数 : %d" % (iris.data.shape[0],(iris.target != y_pred).sum()))
from sklearn.naive_bayes import BernoulliNB
clf = BernoulliNB()
clf = clf.fit(iris.data, iris.target)
y_pred=clf.predict(iris.data)
print("伯努利朴素贝叶斯，样本总数： %d 错误样本数 : %d" % (iris.data.shape[0],(iris.target != y_pred).sum()))
