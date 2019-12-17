# # 实现SVM对手写数字的识别
# from sklearn import datasets  # 从skleran.datasets里有导入手写体数字加载器
# from sklearn.model_selection import train_test_split  # 导入train_test_split用于数据分割
# from sklearn.preprocessing import StandardScaler  # 导入标准化数据
# from sklearn.svm import LinearSVC  # 从sklearn.svm中导入基于现行假设的支持向量机分类器LinearSVC
# from sklearn.metrics import classification_report
#
# # 1.数据获取
# digits = datasets.load_digits()  # 从通过数据加载器获得手写数字的数码图像数据并存储在digits中
# print(digits.data.shape)  # 检视数据规模和数据纬度
#
# # 2.数据预处理：训练集测试集分割，数据标准化
# X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=33)
# print(X_train)
# print(y_train)
# print(y_train.shape)
# ss = StandardScaler()  # 对测试集和训练集进行标准化
# X_train = ss.fit_transform(X_train)
# X_test = ss.transform(X_test)
#
# # 3.使用SVM训练
# lsvc = LinearSVC()  # 初始化现行假设的支持向量机分类器 LinearSVC
# lsvc.fit(X_train, y_train)  # 进行模型训练
# y_predict = lsvc.predict(X_test)
#
# # 4.生成结果报告
# print('The Accuracy of Linear SVC is %f' % lsvc.score(X_test, y_test))  # 使用自带的模型评估函数进行准确性评测



# 鸢尾花的数据
from sklearn import datasets
from sklearn import svm
# 使用交叉验证的方法，将数据集分为训练集与测试集
from sklearn.model_selection import train_test_split


# 加载iris数据集
def load_data():
    iris = datasets.load_iris()
    """展示数据集的形状
       diabetes.data.shape, diabetes.target.shape
    """

    # 将数据集拆分为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.10, random_state=0)
    return X_train, X_test, y_train, y_test


# 使用LinearSVC考察线性分类SVM的预测能力
def test_LinearSVC(X_train, X_test, y_train, y_test):
    # 选择模型
    cls = svm.LinearSVC()

    # 利用训练数据训练模型
    cls.fit(X_train, y_train)
    # 训练好的参数


    print('Coefficients:%s \n\nIntercept %s' % (cls.coef_, cls.intercept_))

    # 利用测试数据评判模型
    print('\n\nScore: %.2f' % cls.score(X_test, y_test))


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_data()
    test_LinearSVC(X_train, X_test, y_train, y_test)
