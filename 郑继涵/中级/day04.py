'''

大家都听过老和尚讲的故事吧，从前有座山，山上有座庙，庙里有个老和尚，老和尚在讲故事给小和尚听：
"从前有座山，山上有座庙，庙里有个老和尚，老和尚在讲故事给小和尚听：'从前座山，山上有座庙，庙里有个老和尚，老和尚在讲故事给小和尚听........."，

递归使用   递归指的是调用自己的函数

import sys
sys.setrecursionlimit(1000000) #例如这里设置为十万
i = 0
def fact():
    global i
    i += 1
    print("fact%d"%i)
    fact()
fact()

阶乘  先让学生写一个100！

f(n)=n*(n-1)*(n-2)*...*1

# 此函数展示的是递归阶乘的计算
def fact(x):
    if x==1:
        return 1
  # else:
  #     return x*fact(x-1)
  # return x*fact(x-1)
print(fact(5))
！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！


2.2汉诺塔
汉诺塔问题是递归函数的经典应用，它来自一个古老传说：在世界刚被创建的时候有一座钻石宝塔A，其上有64个金蝶。
所有碟子按从大到小的次序从塔底堆放至塔顶。紧挨着这座塔有另外两个钻石宝塔B和C。
从世界创始之日起，波罗门的牧师就一直在试图把塔A上的碟子移动到C上去，其间借助于塔B的帮助。
每次只能移动一个碟子，任何时候都不能把一个碟子放在比它小的碟子上面。当牧师们完成这个任务时，世界末日也就到了。
对于汉诺塔问题的求解，可以通过以下3步实现：
（1）将塔A上的n -1个碟子借助C塔先移动到B塔上；
（2）把塔A上剩下的一个碟子移动到塔C上；
（3）将n - 1个碟子从B塔借助塔A移动到塔C上。
很显然，这是一个递归求解的过程，假设碟子数n=3时，汉诺塔问题的求解过程如下图所示：


汉诺塔的递归算法（Python实现）：

def Hanoi(n, A, B, C) :
  if (n == 1) :
    move(A, c)   #表示只有一个碟子时，直接从A塔移动到C塔
  else :
    Hanoi(n - 1, A, C, B)  #将剩下的A塔上的n-1借助C塔移动到B塔
    move(A, C)              #将A上最后一个直接移动到C塔上
    Hanoi(n - 1, B, A, C)  #将B塔上的n-1个碟子借助A塔移动到C塔


汉诺塔的递归算法代码实现：

#coding=utf-8

i = 1
def move(n, mfrom, mto) :
  global i
  print "第%d步:将%d号盘子从%s -> %s" %(i, n, mfrom, mto)
  i += 1

def hanoi(n, A, B, C) :
  if n == 1 :
    move(1, A, C)
  else :
    hanoi(n - 1, A, C, B)
    move(n, A, C)
    hanoi(n - 1, B, A, C)

#********************程序入口**********************
try :
  n = int(raw_input("please input a integer :"))
  print "移动步骤如下："
  hanoi(n, 'A', 'B', 'C')
except ValueError:
  print "please input a integer n(n > 0)!"


！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
斐波那契数列：亦称之为斐波那契数列（意大利语： Successione di Fibonacci)，又称黄金分割数列
斐波拉契数列，是这样的一个数列：0、1、1、2、3、5、8、13、21、……。
斐波拉契数列的核心思想是:
从第三项起，每一项都等于前两项的和，即F(N) = F(N - 1) + F(N - 2) (N >= 2)
并且规定F(0) = 0，F(1) = 1
通向公式为：f(n)=f(n-1)+f(n-2)

 ————————————————
# 此函数展示的fabonic
def fabonic(n):
    if n<1:
        return 1
    elif n==1 or n==2:
        return 1
    else:
        return fabonic(n-1)+fabonic(n-2)

print(fabonic(8))
 ————————————————

非递归实现：
def Fibnacci(n):
    result = [0,1]
    if n <= 1:
        return result[n]
    for i in range(2,n+1):
        result.append(result[i-1]+result[i-2])
    return result[n]
-----------------------------------------------------
def fab(n):  
    n1 = 1      
    n2 = 1      
    n3 = 1    

    if n < 1:  
        print('输入有误！')
    
    while (n-2) > 0:    
        n3 = n2 + n1   #第三项为前两项和
        n1 = n2            #计算完，整体后移，准备计算下一项  
        n2 = n3            
        n -= 1              

    return n3            

a = int(input('请输入要计算的斐波那契项数：'))
result = fab(a)
print('第%d项斐波那契数为%d' % (a, result))


'''