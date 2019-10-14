'''
时间复杂度 定义：如果一个问题的规模是n，解这一问题的某一算法所需要的时间为T(n)，它是n的某一函数 T(n)称为这一算法的“时间复杂性”。

二、计算方法
1.一个算法执行所耗费的时间，从理论上是不能算出来的，必须上机运行测试才能知道。
但我们不可能也没有必要对每个算法都上机测试，
只需知道哪个算法花费的时间多，哪个算法花费的时间少就可以了。
并且一个算法花费的时间与算法中语句的执行次数成正比例，哪个算法中语句执行次数多，它花费时间就多。
一个算法中的语句执行次数称为语句频度或时间频度。记为T(n)。
2.一般情况下，算法的基本操作重复执行的次数是模块n的某一个函数f（n），
因此，算法的时间复杂度记做：T（n）=O（f（n））。
随着模块n的增大，算法执行的时间的增长率和f（n）的增长率成正比，所以f（n）越小，
算法的时间复杂度越低，算法的效率越高。
在计算时间复杂度的时候，先找出算法的基本操作，然后根据相应的各语句确定它的执行次数，
再找出T（n）的同数量级
（它的同数量级有以下：1，Log2n ，n ，nLog2n ，n的平方，n的三次方，2的n次方，n！），
找出后，f（n）=该数量级，若T(n)/f(n)求极限可得到一常数c，
则时间复杂度T（n）=O（f（n））。
3.常见的时间复杂度
按数量级递增排列，常见的时间复杂度有：
常数阶O(1),  对数阶O(log2n),  线性阶O(n),  线性对数阶O(nlog2n),  平方阶O(n^2)， 立方阶O(n^3),...， k次方阶O(n^k), 指数阶O(2^n) 。

例：算法：
输出乘法口诀表(九九表)

Version: 0.1
Author: 骆昊
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()

    则该算法的 时间复杂度：T（n）=O（n^2)

        O(1)    简单的一次运算
        O(logn)    循环减半
        O(n)    一次循环
        O(nlogn)    一个循环加一个循环减半
        O(n^2)     两个循环
        O(n^2logn)
        O(n^3)

'''

'''
查看执行时间
import time
end = time.process_time()
print("%s" %(end))
！！！！！！！！！！！！！！！！！！！！！
# import time
# t1 = time.clock()
# sum = 0
# for i in range(9999999):
#     sum = sum +1
# time.sleep(1)
# print(time.clock()-t1)


排序
1.冒泡排序
原理：列表中两个相邻的数，如果前一个数比后一个数大，就做交换。一共需要遍历列表的次数是len(lst)-1

def bubble_sort(lst):
    for i in range(len(lst)-1):     # 这是需要循环遍历多少次
        for j in range(len(lst)-i-1):   # 每次数组中的无序区
            if lst[j] >lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
 
lst = [1, 2, 44, 3, 5]
bubble_sort(lst)
print(lst)

冒泡排序的最差情况，即每次都交互顺序的情况，时间复杂度是O(n2)

2、选择排序
　　　　原理：每次遍历找到当下数组最小的数，并把它放到第一个位置，下次遍历剩下的无序区
def select_sort(lst):
    for i in range(len(lst) - 1):    # 当前需遍历的次数
        min_loc = i     # 当前最小数的位置
        for j in range(i+1, len(lst)):   # 无序区
            if lst[j] < lst[min_loc]:     # 如果有更小的数
                min_loc = j     # 最小数的位置改变
        if min_loc != i:
            lst[i], lst[min_loc] = lst[min_loc], lst[i]     # 把最小数和无序区第一个数交换交换
 
lst = [1, 2, 44, 3, 5]
select_sort(lst)
print(lst)
　　

4、快速排序

思路：取第一个元素，让它归位，就是放到一个位置，使它左边的都比它小，右边的都比它大，
时间复杂度：O(nlog(n))
最坏情况：最坏情况下的事件复杂度是O(n2)            
              
def parttion(lst, left, right):
    i = left
    j = right
    tmp = lst[i]    # 把此次循环的标志数存起来
    while i < j:
        while i < j and lst[j] > tmp:   # 先从右边开始找比标志数小的，有的话跳出循环
            j -= 1
        lst[i] = lst[j] # 跳出循环之后，把这个比标志数小的值放到标志数的位置
        while i < j and lst[i] < tmp:   # 左边的排序方法和右边一样
            i += 1
        lst[j] = lst[i]
    lst[i] = tmp    # 整个排序结束之后，把一开始的标志数放回空位
    return i
 
 
def quick_sort(lst, left, right):
    if left < right:    # 至少有两个元素
        p = parttion(lst, left, right)
        quick_sort(lst, left, p-1)
        quick_sort(lst, p+1, right)
         
 
lst = [1, 2, 44, 3, 5]
quick_sort(lst, 0, 4)
print(lst)


# 查找
顺序查找
    这个没的说，就是for循环呗，时间复杂度O(n)
> def sequential_Search(item,list): 	
>		i = 0 	
>		while i < len(list): 		
> 			if item == list[i]:
> 				return i 		
> 			i += 1 	
>		return -1


二分查找(折半查找)时间复杂度O(logn)
就是一半一半的查找，看目标值在左边一半还是右边一半，然后替换左端点或者右端点，继续判断


def binary_serach(li,val):
    low = 0
    high = len(li)-1
    while low <= high:
        mid = (low+high)//2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            high = mid-1
        else:
            low = mid+1
    else:
        return None

'''