# 定义函数
def my_abs(x):
    if not isinstance(x, (int, float)): # 参数类型做检查
        # pass # pass占位符
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs('-13'))

#  定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

#  关键字参数
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict
# kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

extra = {'city': 'Shanghai', 'jbo': 'Engineer'}
person('Trump', 24, **extra) # 'name:'Trump 'age:' 24 'other:' {'city': 'Shanghai', 'jbo': 'Engineer'}

# 命名关键字参数
# 限制关键字参数的名字，用一个特殊分隔符*，*后面的参数被视为命名关键字参数
def people(name, age, *, city, job):
    print(name, age, city, job)

people('Baozi', 24, city='Bejing', job='Police') 

# 参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =',b, 'c =',c, 'args =', args, 'kw =', kw)
f1(1, 3, 5, 'a', 'b', x=33) # a=1 b =3 c = 5 args=('a', 'b') kw = {'x': 33}