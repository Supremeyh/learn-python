# 面向对象高级编程

# 数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。
# 在Python中，面向对象还有很多高级特性，允许我们写出非常强大的功能。我们会讨论多重继承、定制类、元类等概念。

# __slots__
# 在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

s = Student() # 创建新的实例
s.name = 'Bruce' # 绑定属性'name'
s.score = 89 # 报错， AttributeError: 'Student' object has no attribute 'score'

# 注意__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。



