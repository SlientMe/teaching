# -*- coding: utf-8 -*-
# @Time : 2019/10/14 17:09
# @Author : liuqi
# @FileName: day1.py
# @Software: PyCharm
# 简单的说，类是对象的蓝图和模板，而对象是类的实例。
# 这个解释虽然有点像用概念在解释概念，但是从这句话我们至少可以看出，
# 类是抽象的概念，而对象是具体的东西。在面向对象编程的世界中，一切皆为对象，
# 对象都有属性和行为，每个对象都是独一无二的，而且对象一定属于某个类（型）
# 。当我们把一大堆拥有共同特征的对象的静态特征（属性）和动态特征（行为）
# 都抽取出来后，就可以定义出一个叫做“类”的东西。
'''
在Python中可以使用`class`关键字定义类，然后在类中通过之前学习过的函数来
定义方法，这样就可以将对象的动态特征描述出来，

类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。

'''

class Student(object):
    # 类有一个名为_init__()的特殊方法（构造方法）
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)

# self代表类的实例，而非类
# 写在类中的函数，我们通常称之为（对象的）方法，这些方法就是对象可以
# 接收的消息。

# 当我们定义好一个类之后，可以通过下面的方式来创建对象并给对象发消息。

def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('骆昊', 38)
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_movie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()


if __name__ == '__main__':
    main()
'''
因为在很多面向对象编程语言中，我们通常会将对象的属性设置为私有的
（private）或受保护的（protected），简单的说就是不允许外界访问，
而对象的方法通常都是公开的（public），因为公开的方法就是对象能够
接受的消息。在Python中，属性和方法的访问权限只有两种，也就是公开的
和私有的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为
开头，下面的代码可以验证这一点。
'''

'''
class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print(test.__foo)


if __name__ == "__main__":
    main()
'''
# 但是，Python并没有从语法上严格保证私有属性或方法的私密性，它只是给私有的属性和
# 方法换了一个名字来“妨碍”对它们的访问，事实上如果你知道更换名字的规则仍然可以访
# 问到它们，
'''
class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()
在实际开发中，我们并不建议将属性设置为私有的，因为这会导致子类无法访问（后面会讲到）
'''