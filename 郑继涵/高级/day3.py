# -*- coding: utf-8 -*-
# @Time : 2019/10/14 17:16
# @Author : liuqi
# @FileName: day2.py
# @Software: PyCharm
### 面向对象的支柱
'''
面向对象有三大支柱：封装、继承和多态。后面两个概念在下一个章节中进行详细的
说明，这里我们先说一下什么是封装。我自己对封装的理解是“隐藏一切可以隐藏
的实现细节，只向外界暴露（提供）简单的编程接口”。我们在类中定义的方法其
实就是把数据和对数据的操作封装起来了，在我们创建了对象之后，只需要给对象
发送一个消息（调用方法）就可以执行方法中的代码，也就是说我们只需要知道
方法的名字和传入的参数（方法的外部视图），而不需要知道方法内部的实现细节
（方法的内部视图）。

### 类之间的关系

简单的说，类和类之间的关系有三种：is-a、has-a和use-a关系。

- is-a关系也叫继承或泛化，比如学生和人的关系、手机和电子产品的关系都属于继承关系。

- has-a关系通常称之为关联，比如部门和员工的关系，汽车和引擎的关系都属于关联关系；
关联关系如果是整体和部分的关联，那么我们称之为聚合关系；如果整体进一步负责了部分的生命周期
（整体和部分是不可分割的，同时同在也同时消亡），那么这种就是最强的关联关系，我们称之为合成关系。

- use-a关系通常称之为依赖，比如司机有一个驾驶的行为（方法），其中（的参数）使用到了汽车，那么司机和汽车的关系就是依赖关系。
利用类之间的这些关系，我们可以在已有类的基础上来完成某些操作，也可以在已有类的基础上创建新的类，
这些都是实现代码复用的重要手段。复用现有的代码不仅可以减少开发的工作量，也有利于代码的管理和维护，
这是我们在日常工作中都会使用到的技术手段。

'''

'''
### 继承和多态
刚才我们提到了，可以在已有类的基础上创建新类，这其中的一种做法就是让一个类从另
一个类那里将属性和方法直接继承下来，从而减少重复代码的编写。提供继承信息的我们称之为父类
，也叫超类或基类；得到继承信息的我们称之为子类，也叫派生类或衍生类。子类除了继承父类提供的属性和方法，
还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力，在实际开发中，我们经常会用子类对象去
替换掉一个父类对象，这是面向对象编程中一个常见的行为，对应的原则称之为
'''

'''
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
 
#多重继承
class sample(speaker,student):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
 
test = sample("Tim",25,80,4,"Python")
test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法
'''

'''
继承 与 多继承 
class Person(object):
    """人"""
    def __init__(self, name, age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age
    def play(self):
        print('%s正在愉快的玩耍.' % self._name)
    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)

class Student(Person):
    """学生"""
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self, grade):
        self._grade = grade
    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))


class Teacher(Person):
    """老师"""
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title
    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))

def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('骆昊', 38, '老叫兽')
    t.teach('Python程序设计')
    t.watch_av()


if __name__ == '__main__':
    main()
'''

'''
子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override）。
通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，当我们调用这个经过子类重写的方法时，
不同的子类对象会表现出不同的行为，这个就是多态（poly-morphism）。

'''
'''
from abc import ABCMeta, abstractmethod
class Pet(object, metaclass=ABCMeta):
    """宠物"""
    def __init__(self, nickname):
        self._nickname = nickname
    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass
class Dog(Pet):
    """狗"""
    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)
class Cat(Pet):
    """猫"""
    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)
def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()
if __name__ == '__main__':
    main()
'''

