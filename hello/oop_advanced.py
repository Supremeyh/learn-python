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







