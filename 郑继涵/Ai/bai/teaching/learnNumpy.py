import numpy as np
'''
 # 矩阵 在数学中，矩阵（Matrix）是一个按照长方阵列排列的复数或实数集合
 由 m × n 个数aij排成的m行n列的数表称为m行n列的矩阵，简称m × n矩阵。记作：
 这m×n 个数称为矩阵A的元素，简称为元，数aij位于矩阵A的第i行第j列，称为矩阵A的(i,j)元，
 以数 aij为(i,j)元的矩阵可记为(aij)或(aij)m × n，m×n矩阵A也记作Amn。

'''
# https://blog.csdn.net/a373595475/article/details/79580734
a = np.array([1,2,3])
b = np.array([[1,  2], [3,  4]],dtype="float")
print (a)
print (b)

# ndarray.shape 这一数组属性返回一个包含数组维度的元组，它也可以用于调整数组大小。
print(b.shape)


c = np.array([[1,2,3],[4,5,6]])
cc = c.reshape(3,2)
print(c)
print(cc)

# ndarray.ndim 这一数组属性返回数组的维数。
a = np.arange(24)
print(a)
print(a.ndim)
b = a.reshape(2,-1)
print(b)
print(b.ndim)

# NumPy - 数组创建例程
print(np.zeros(10,dtype=float))

print(np.zeros(shape=(3,5)))

print(np.ones(shape=(3,5)))

print(np.full(shape=(6,5),fill_value=5))

# NumPy - 来自现有数据的数组
x =  [1,2,3]
a = np.asarray(x)
print(a)

x =  [1,2,3]
a = np.asarray(x, dtype =  float)
print(a)


# 内置的range()函数返回列表对象。 此列表的迭代器用于形成ndarray对象
# numpy.arange(start, stop, step, dtype)
list = np.arange(5,dtype="float")
print(list)

# numpy.linspace 此函数类似于arange()函数。 在此函数中，指定了范围之间的均匀间隔数量，
# 而不是步长。 此函数的用法如下。  numpy.linspace(start, stop, num, endpoint, retstep, dtype)
# num 要生成的等间隔样例数量，默认为50num 要生成的等间隔样例数量，默认为50

import numpy as np
x = np.linspace(10,20,5)
print(x)


# vNumPy - 切片和索引
# ndarray对象的内容可以通过索引或切片来访问和修改，就像 Python 的内置容器对象一样。
#通过将由冒号分隔的切片参数（start:stop:step）直接提供给ndarray对象，也可以获得相同的结果。
a = np.arange(10)
b = a[5]
print(b)

a = np.arange(10)
print(a[2:])
print(a[2:5])
b = a[2:7:2]
print(b)

#  上面的描述也可用于多维ndarray。
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a[1:,:])
print(a[:,-1])  # 最后一列

#########################
matrix = np.linspace(1,30,12).reshape(3,-1)
print(matrix)
print(matrix[0,matrix[0,:]>5])   # 第一行所有比5大的数
print(matrix[matrix[:,3]>9,3])  # 第3列比9大的数
##############################

x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print(x[1:4,1:3])

print(x[x >5])   #  布尔索引      '大于 5 的元素是：'

# NumPy 矩阵的运算
# 术语广播是指 NumPy 在算术运算期间处理不同形状的数组的能力。 对数组的算术运算通常
# 在相应的元素上进行。 如果两个阵列具有完全相同的形状，则这些操作被无缝执行。
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a * b
d = np.dot(a,b)
print(c)

a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]])
b = np.array([1.0,2.0,3.0])
print(a+b)

a = np.arange(0,60,5)
a = a.reshape(3,4)
print(a.T)  # 转置


# 数组的连接
# concatenate 沿着现存的轴连接数据序列
# hstack 水平堆叠序列中的数组（列方向）
# vstack 竖直堆叠序列中的数组（行方向）

# numpy.concatenate数组的连接是指连接。 此函数用于沿指定轴连接相同形状的两个或多个数组。
# 该函数接受以下参数。  numpy.concatenate((a1, a2, ...), axis)  axis默认为0
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(np.concatenate((a,b)))
print(np.vstack((a,b)))
print(np.concatenate((a,b),axis=1))
print(np.hstack((a,b)))

# 数组分割
# split 将一个数组分割为多个子数组
#	hsplit 将一个数组水平分割为多个子数组（按列）
#	vsplit 将一个数组竖直分割为多个子数组（按行）
a = np.arange(9)
print(np.split(a,3))   # '将数组分为三个大小相等的子数组：'
print(np.split(a,[4,7]))  # '将数组在一维数组中表明的位置分割：'

# numpy.hsplit是split()函数的特例，其中轴为 1 表示水平分割，无论输入数组的维度是什么。
a = np.arange(16).reshape(4,4)
print(np.hsplit(a,2)) # 水平分割
print(np.vsplit(a,2)) # 竖直分割


# 三角函数  它为弧度制单位的给定角度返回三角函数比值。
a = np.array([0,30,45,60,90])
# 通过乘 pi/180 转化为弧度
print(np.sin(a*np.pi/180))
print(np.cos(a*np.pi/180))
print(np.tan(a*np.pi/180))

# 舍入函数
a = np.array([1.0,5.55,  123,  0.567,  25.532])
print(np.around(a))
print(np.around(a, decimals=1))
# numpy.floor()  返回不大于输入参数的最大整数
a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
print(np.floor(a))
# numpy.ceil()  ceil()函数返回输入值的上限
print(np.ceil(a))


# NumPy - 算数运算
a = np.arange(9, dtype = np.float_).reshape(3,3)
b = np.array([10,10,10])
print(np.add(a,b))  # 矩阵和向量相加
print(np.subtract(a,b)) # 相减
print(np.multiply(a,b)) #
print(np.divide(a,b))


# NumPy - 统计函数
# numpy.amin() 和 numpy.amax()  这些函数从给定数组中的元素沿指定轴返回最小值和最大值。
a = np.array([[3,7,5],[8,4,3],[2,4,9]])
print(np.amax(a,axis=0))
# numpy.mean() 均值
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))
# 方差 var
print(np.var([1,2,3,4]))
# 排序 sort  .argsort()
a = np.array([[3,7],[9,1]])
print(np.sort(a[:,1], axis =  0))

print(np.random.randint(1,100,size=100))

T = np.random.normal(0,1,size=100000)
print(np.mean(T))
print(np.std(T))















