''''
我们讲到这里，不知道大家是否已经意识到，Python是一门[动态语言]
通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，
当然也可以对已经绑定的属性和方法进行解绑定。但是如果我们需要限
定自定义类型的对象只能绑定某些属性，可以通过在类中定义\_\_slots\_\_变
量来进行限定。需要注意的是\_\_slots\_\_的限定只对当前类的对象生效，对子类并不起任何作用。
'''
'''
先来谈一下类属性和实例属性

在前面的例子中我们接触到的就是实例属性（对象属性），顾名思义，
类属性就是类对象所拥有的属性，它被所有类对象的实例对象所共有，在内存中只存在一个副本，
这个和C++中类的静态成员变量有点类似。对于公有的类属性，在类外可以通过类对象和实例对象访问
class Student():
    time = 0 
    def __init__(self,name):
        self.name = name
        Student.time += 1
    def study(self):
        print("study")

s = Student("tim")
s1 = Student("Jack")
print(Student.time)

'''

'''
### 静态方法和类方法
类属性与方法
类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。

类的私有方法实例如下：


之前，我们在类中定义的方法都是对象方法，也就是说这些方法都是发送给对象的消息。
实际上，我们写在类中的方法并不需要都是对象方法，例如我们定义一个“三角形”类，
通过传入三条边长来构造三角形，并提供计算周长和面积的方法，但是传入的三条边长未必能构造出三角形对象，
因此我们可以先写一个方法来验证三条边长是否可以构成三角形，这个方法很显然就不是对象方法，
因为在调用这个方法时三角形对象尚未创建出来（因为都不知道三条边能不能构成三角形），
所以这个方法是属于三角形类而并不属于三角形对象的。我们可以使用静态方法来解决这类问题，代码如下所示。
静态方法可以理解为就是类方法少了cls。
'''
'''
from math import sqrt
class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))
def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形.')
if __name__ == '__main__':
    main()
'''

'''
和静态方法比较类似，Py它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象）
thon还可以在类中定义类方法，类方法的第一个参数约定名为cls，
，通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象，代码如下所示。
首先我们有一个需求;商品的折扣是人为定的，与商品中的对象无关。即Goods中的折扣直接通过Goods去更改，
而不是要先创建一个Goods对象再去改。因为这个折扣将对所有的商品生效的。上面的代码显示：要先有了apple的基础上才能去
更改discount。如果再创建一个”banana“商品，其折扣仍旧是0.5，显示这不是我们想要的效果。
class Goods:
    __discount=0.5
    def __init__(self,name,price):
        self.name=name
        self.__price=price
    @property
    def price(self):
        return self.__price*self.__discount
    def set_price(self,new_price):
        if new_price and type(new_price) is int:  #这里保护了输入的数据为合法数据
            self.__price=new_price
        else:
            print('请输入正确的价格数据')

    @classmethod
    def set_discount(cls,new_discount): #将self替代为cls，用于这个类
        cls.__discount=new_discount
        return self.__discount
apple=Goods('苹果',6)
Goods.set_discount(0.8)
print(apple.price)
'''