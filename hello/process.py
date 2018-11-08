# 进程和线程

# “多任务”,简单地说，就是操作系统可以同时运行多个任务。
# 真正的并行执行多任务只能在多核CPU上实现，但是，由于任务数量远远多于CPU的核心数量，所以，操作系统也会自动把很多任务轮流调度到每个核心上执行。

# 对于操作系统来说，一个任务就是一个进程（Process）
# 在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）。
# 线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。

# 多任务的实现有3种方式： 多进程模式multiprocessing; 多线程模式；多进程+多线程模式。多进程和多线程的程序涉及到同步、数据共享的问题，编写起来更复杂。

# 多进程模式 fork()，调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
# 子进程永远返回0，而父进程返回子进程的ID。
import os

print('process (%s) start ...' % os.getpid() )
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 运行结果如下：
Process (876) start...
I (876) just created a child process (877).
I am child process (877) and my parent is 876.

# 在Unix/Linux下，可以使用fork()调用实现多进程。Mac系统是基于BSD（Unix的一种）内核。Windows没有fork调用，上面的代码在Windows上无法运行。
# 要实现跨平台的多进程，可以使用multiprocessing模块。
# 进程间通信是通过Queue、Pipes等实现的。


# 多线程
# _thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
# 由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，
# 它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。名字仅仅在打印时用来显示，
# 完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……

# Lock
# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，
# 所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
# 创建一个锁就是通过threading.Lock()来实现
# 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。

# ThreadLocal
# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
# 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。


# 计算密集型 vs. IO密集型
# 多进程和多线程，这是实现多任务最常用的两种方式
# 要实现多任务，通常我们会设计Master-Worker模式，Master负责分配任务，Worker负责执行任务，因此，多任务环境下，通常是一个Master，多个Worker。
# 多进程模式最大的优点就是稳定性高,缺点是创建进程的代价大
# 任务分为计算密集型和IO密集型,计算密集型任务的特点是要进行大量的计算，消耗CPU资源,因此，代码运行效率至关重要。
# Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写。
# IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，CPU消耗很少，任务的大部分时间都在等待IO操作完成。常见的大部分任务都是IO密集型任务，比如Web应用。
# 对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。

# 异步IO
# 现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，
# 这种全新的模型称为事件驱动模型，Nginx就是支持异步IO的Web服务器，它在单核CPU上采用单进程模型就可以高效地支持多任务。
# 在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。由于系统总的进程数量十分有限，因此操作系统调度非常高效。
# 用异步IO编程模型来实现多任务是一个主要的趋势。
# 对应到Python语言，单线程的异步编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。


# 分布式进程
# 在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。
# Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，
# 依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。






















