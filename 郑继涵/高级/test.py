class Person(object):
    """人"""
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)
    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)

class Student():
    """学生"""
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade
    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))
    def play(self):
        print('%s正在悲伤的玩耍.' % self.name)


class Teacher(Student,Person):
    """老师"""
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title
    def title(self, title):
        self._title = title
    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))

llvbbo = Teacher('llvbbo',16,'good')
llvbbo.play()