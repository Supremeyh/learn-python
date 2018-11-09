# collections

# collections是Python内建的一个集合模块，提供了许多有用的集合类。

# namedtuple, namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
from collections import namedtuple
# 如表示一个点的二维坐标
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2) 
 

# deque， 为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
q # deque(['y', 'a', 'b', 'c', 'x])


# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
dd['key1'] # 'abc' key1存在
dd['key2'] # 'N/A' key2不存在


# OrderedDict，使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。可以用OrderedDict保持Key的顺序.
# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序。OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key。


# ChainMap
# ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
# 什么时候使用ChainMap最合适？举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。
# 我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。


# Counter， 一个简单的计数器。
# 例如，统计字符出现的个数
from collections import Counter
for x in 'supremeyh':
  c[x] = c[x] + 1
c  # Counter({'e': 2, 's': 1, 'u': 1, 'p': 1, 'r': 1, 'm': 1, 'y': 1, 'h': 1}) # Counter实际上也是dict的一个子类












