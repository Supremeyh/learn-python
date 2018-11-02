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


# @property装饰器
# 负责把一个方法变成属性调用, 给函数动态加上功能,既能检查参数，又可以用类似属性这样简单的方式来访问类的变量
class Teacher(object):
    @property # 把一个getter方法变成属性，只需要加上@property就可以了
    def age(self): 
        return self._age
    
    @age.setter # @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值,拥有一个可控的属性操作
    def age(self.value):
        if not isinstance(value, int):
            raise ValueError('age must be an integer!')
        if value < 1 or value > 100:
            raise ValueError('age must between 1 - 100')
        self._age = value

# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性.

