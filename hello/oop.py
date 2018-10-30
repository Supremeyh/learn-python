# 面向过程的程序设计,把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，
# 即把大块函数通过切割成小块函数来降低系统的复杂度。

# 面向对象编程,OOP,Object Oriented Programming,一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
# 面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，
# 计算机程序的执行就是一系列消息在各个对象之间传递。

# 所以，面向对象的设计思想是抽象出Class，根据Class创建Instance，面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。

# 数据封装、继承和多态是面向对象的三大特点。

# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。


# 首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，这个对象拥有name和score这两个属性（Property）
# 如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。
class Student(object):

    def __init__(self, name, score): # __init__方法的第一个参数永远是self，表示创建的实例本身
        self.name = name
        self.score = score

    def print_score(self): # 第一个参数永远是实例变量self
        print('%s: %s' %(self.name, self.score))
    
# 给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法Method
# 面向对象编程的一个重要特点就是数据封装。在一个Student类中，每个实例就拥有各自的数据。
lisa = Student('Lisa Simpson', 88)
lisa.print_score()

# 访问限制
class Teacher(object):
    def __init__(self, name, age):
        self.__name = name # 实例的变量名如果以__开头，就变成了一个私有变量（private）,内部属性不被外部访问
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if 0 <= age <= 100:
            self.__age = age
        else:
            raise ValueError('bad age')

# 特殊变量 ,__xxx__ , 双下划线且以双下划线结尾,可以直接访问的
# 私有变量 ,__xxx , 双下划线,可以直接访问的, 内部属性不被外部访问. 因Python解释器对外把__name变量改成了_Student__name，
# 故仍然可以通过_Student__name来访问__name变量。 Python本身没有任何机制阻止你干坏事，一切全靠自觉


# 继承可以把父类的所有功能都直接拿过来，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
# 多态，一种接口，多种实现，实现代码重用，接口重用；
# 动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。





    


