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
'''