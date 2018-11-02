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



# 多重继承
# 一个子类就可以同时获得多个父类的所有功能
class Dog(Mammal, Runnable):
    pass

# 把继承关系先构成一张图;利用拓扑排序的方法输出拓扑顺序,并列关系时遵循取最左原则;python继承顺序遵循C3算法，只要在一个地方找到了所需的内容，就不再继续查找
# 拓扑排序（Topological Sorting）,是一个有向无环图（DAG, Directed Acyclic Graph）的所有顶点的线性序列。且该序列必须满足下面两个条件：
# 每个顶点出现且只出现一次; 若存在一条从顶点 A 到顶点 B 的路径，那么在序列中顶点 A 出现在顶点 B 的前面。
# 有向无环图（DAG）才有拓扑排序，非DAG图没有拓扑排序一说, 通常，一个有向无环图可以有一个或多个拓扑排序序列。

# 一个DAG 图，那么如何写出它的拓扑排序呢？这里说一种比较常用的方法：
# 从 DAG 图中选择一个 没有前驱（即入度为0）的顶点并输出。
# 从图中删除该顶点和所有以它为起点的有向边。
# 重复 1 和 2 直到当前的 DAG 图为空或当前图中不存在无前驱的顶点为止。后一种情况说明有向图中必然存在环。

# 所谓顶点的度(degree)，就是指和该顶点相关联的边数, 入度(in-degree)以某顶点为弧头，终止于该顶点的弧的数目称为该顶点的入度,
# 也即以顶点V为头的弧的数目称为V的入度(InDegree)，记为ID(V))



# MixIn
# 给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，
# 通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

# 编写一个多进程模式的TCP服务，定义如下：
class MyTCPServer(TCPServer, ForkingMixIn):
    pass
# 编写一个多线程模式的UDP服务，定义如下：
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
# 这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。



# __str__()和__repr__()
# __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
# 打印出来的实例，不但好看，而且容易看出实例内部重要的数据。
class School(object):
    def __init__(self, name):
        self.name = name 
    def __str__(self):
        return 'School object (name=%s)' % self.name
    __repr__ = __str__


# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环。
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b
    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 10000:  # 退出循环的条件
            raise StopIteration() 
        return self.a  # 返回下一个值

# 把Fib实例作用于for循环
for n in Fib():
    print(n)
# 1 1 2 3 5 8 13 21 ... 6765


# __getitem__
# 像list那样按照下标取出元素, 传入的参数可能是一个int，也可能是一个切片对象slice,所以要做判断
def Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

# 现在，就可以按下标访问数列的任意一项了：
f = Fib()
f[10] # 89
f[:5] # 1, 1, 2, 3, 5

# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
# 通过上面的方法，自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。


# __getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
# 写一个__getattr__()方法，动态返回一个属性

# 利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, attr):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
# 这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
Chain().status.user.timeline.list  #'/status/user/timeline/list'
# REST API会把参数放到URL中，比如GitHub的API: GET /users/:user/repos 调用时，需要把:user替换为实际用户名
Chain().users('sea').repos #  '/users/sea/repos'


# __call__
# 直接对实例进行调用自己的属性和方法
class Book(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('the book name is %s.' % self.name)
# 调用方式如下：
b = Book('Game of Thrones')
b()  # self参数不要传入. the book name is Game of Thrones.

# 判断一个对象是否是“可调用” ?通过callable()函数
callable(Book()) # True


# 枚举类
# Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
from enum import Enum

Month = Enum('Month',  ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
# 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
# Jan => Month.Jan , 1    Feb => Month.Feb , 2    ......    Dec => Month.Dec , 12


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique
@unique   # @unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6








