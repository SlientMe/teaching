import numpy as np

# numpy 中的矩阵的操作

# print(np.__version__)
# array = np.array([[1,2,3],[2,3,4]])  # 只能有一种类型
# print(array.dtype)
# array[1][1] = 5.0
# print(array)
#
# l = [i for i in range(10)]
#
# print(l)
#
# print(np.zeros(10,dtype=float))
#
# print(np.zeros(shape=(3,5)))
#
# print(np.ones(shape=(3,5)))
#
# print(np.full(shape=(6,5),fill_value=5))
#
# print(np.arange(0,20,2))  # 和 for循环很一样
#
# print(np.linspace(0,20,10))  # 从0开始到20结束，中间等长的截出十个点 ，包括0和20
#
# # random
# print(np.random.randint(1,21))  # 整数
#
# print(np.random.randint(0,20,size=10))
#
# print(np.random.randint(5,21,size=(3,5)))
#
# # 设置一个随机种子，让两次随机数相同
# np.random.seed(5)
# print(np.random.randint(5,21,size=(3,5)))
# np.random.seed(5)
# print(np.random.randint(5,21,size=(3,5)))
#
# # 小数  均匀分布
# print(np.random.random())
# print(np.random.random(10))
# print(np.random.random(size=(3,5)))

# # 正态分布
# print(np.random.normal())
# # 指定均值和方差
# print(np.random.normal(5,10))
#
# print(np.random.normal(5,10,size=(3,5)))
#
# print(np.random)
######################################################################################################
'''
# numpy.array的基本操作
x = np.arange(10)
X = np.arange(15).reshape(3,5)

print(x)
print(X)
# 数组的基本属性
print(x.ndim)  # 查看维度
print(x.shape) #查看是几行几列
print(x.size) # 元素个数

# 数据访问
print(x)
print(x[-1])
print(X)
print(X[1][1]) # 不建议
print(X[2,2])  # 推荐
#切片
print(x[0:5])
print(X[:2,:3])  # 前两行的前三列
print(X[0,:])  # X[0] 第一个行
print(X[:,0]) # 第一列
# 子矩阵是直接应用原矩阵的，所以修改子矩阵会影响原矩阵

# 切片后是和原矩阵相关的，修改子矩阵会修改了原矩阵，不相关怎么做 .copy
subX= X[:2,:3].copy()
print(subX)

'''
# 合并操作
x = np.array([1,2,3])
y = np.array([3,2,1])
print(np.concatenate([x,y]))

A = np.array([[1,8,98],
              [9,87,12]])
z = np.array([1,8,265])

print(np.concatenate([A,A]))  # 默认列拼接

print(np.concatenate([A,A],axis=1))# 行拼接

print(np.concatenate([A,z.reshape(1,-1)]))
# 太麻烦，下面是简写
print(np.vstack([A,z]))  # 垂直方向拼接   hstack 水平方向拼接

# 分割操作
x = np.arange(10)
print(x)
x1,x2,x3 = np.split(x,[3,7]) # 从3 和7 开始切分，分成三段

A = np.arange(16).reshape((4,4))
A1,A2 = np.split(A,[2])  # 就是分成了两行
A3,A4 = np.split(A,[2],axis=1)  # 就是分成了两列

upper,lower = np.vsplit(A,[2]) # 垂直切分
left,right = np.hsplit(A,[2]) # 水平切分









