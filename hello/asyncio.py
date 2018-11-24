#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 异步IO
# 当代码需要执行一个耗时的IO操作时，它只发出IO指令，并不等待IO结果，然后就去执行其他代码了。一段时间后，当IO返回结果时，再通知CPU进行处理。
# 异步IO模型需要一个消息循环，在消息循环中，主线程不断地重复“读取消息-处理消息”这一过程
# 当遇到IO操作时，代码只负责发出IO请求，不等待IO结果，然后直接结束本轮消息处理，进入下一轮消息处理过程。当IO操作完成后，将收到一条“IO完成”的消息，
# 处理该消息时就可以直接获取IO操作结果。在“发出IO请求”到收到“IO完成”的这段时间里，同步IO模型下，主线程只能挂起，但异步IO模型下，主线程并没有休息，
# 而是在消息循环中继续处理其他消息。这样，在异步IO模型下，一个线程就可以同时处理多个IO请求，并且没有切换线程的操作。
# 对于大多数IO密集型的应用程序，使用异步IO将大大提升系统的多任务处理能力。

# 老张爱喝茶，煮开水。
# 出场人物：老张，水壶两把（普通水壶，简称水壶；会响的水壶，简称响水壶）。
# 1 老张把水壶放到火上，立等水开。（同步阻塞）
# 老张觉得自己有点傻
# 2 老张把水壶放到火上，去客厅看电视，时不时去厨房看看水开没有。（同步非阻塞）
# 老张还是觉得自己有点傻，于是变高端了，买了把会响笛的那种水壶。水开之后，能大声发出嘀~~~~的噪音。
# 3 老张把响水壶放到火上，立等水开。（异步阻塞）
# 老张觉得这样傻等意义不大
# 4 老张把响水壶放到火上，去客厅看电视，水壶响之前不再去看它了，响了再去拿壶。（异步非阻塞）
# 老张觉得自己聪明了。

# 所谓同步异步，只是对于水壶而言。
# 普通水壶，同步；响水壶，异步。
# 虽然都能干活，但响水壶可以在自己完工之后，提示老张水开了。这是普通水壶所不能及的。
# 同步只能让调用者去轮询自己（情况2中），造成老张效率的低下。

# 所谓阻塞非阻塞，仅仅对于老张而言。
# 立等的老张，阻塞；看电视的老张，非阻塞。
# 情况1和情况3中老张就是阻塞的，媳妇喊他都不知道。虽然3中响水壶是异步的，可对于立等的老张没有太大的意义。所以一般异步是配合非阻塞使用的，这样才能发挥异步的效用。

# 协程，又称微线程，纤程。英文名 coroutine
# 所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
# 第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
# Python对协程的支持是通过generator实现的。在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。
# 但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。
# 传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。
# 如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高：

def consumer():
  r = ''
  while True:
    n = yield r # 返回r, 等待下一次Send, n = Send传递的参数
    if not n:
      return
    print('[consumer] consuming %s... ' %n)
    r = '200 OK'

def produce(c):
  c.send(None)
  n = 0
  while n < 5:
    n = n + 1
    print('[produce] producing %s...' %n)
    r = c.send(n)
    print('[consumer] consuming %s... ' %r)
  c.close()

c = consumer()
produce(c)

# 注意到consumer函数是一个generator，把一个consumer传入produce后：
# 首先调用c.send(None)启动生成器；
# 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
# consumer通过yield拿到消息，处理，又通过yield把结果传回；
# produce拿到consumer处理的结果，继续生产下一条消息；
# produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
# 最后套用Donald Knuth的一句话总结协程的特点：“子程序就是协程的一种特例。”


# 结果：
# [produce] producing 1...
# [consumer] consuming 1...
# [consumer] consuming 200 OK...
# [produce] producing 2...
# [consumer] consuming 2...
# [consumer] consuming 200 OK...
# [produce] producing 3...
# [consumer] consuming 3...
# [consumer] consuming 200 OK...
# [produce] producing 4...
# [consumer] consuming 4...
# [consumer] consuming 200 OK...
# [produce] producing 5...
# [consumer] consuming 5...
# [consumer] consuming 200 OK...


# next() 和 send(None) 相似: send(msg)可以传递yield的值, next()只能传递None。 


# 深入理解 Python yield: https://blog.csdn.net/lftaoyuan/article/details/78915518



# asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。
# asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
# 用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield from调用另一个coroutine实现异步操作。



# async/await
# 为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
# async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换： 把@asyncio.coroutine替换为async；把yield from替换为await，其余的代码保持不变。
import asyncio

@asyncio.coroutine
def hello():
  print('hello python!')
  r = yield from asyncio.sleep(1)  # 异步调用asyncio.sleep(1):
  print('see u again')

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close(
  
)

# 重新编写
async def hello():
  print('hello python!')
  r = await asyncio.sleep(1)
  print('see u again')



# aiohttp
# asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架。
# pip install aiohttp  # 安装aiohttp
import asyncio

from aiohttp import web

async def index(request):
  await asyncio.sleep(0.5)
  return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
  await asyncio.sleep(0.5)
  text = b'<h1>hello, %s!</h1>' % request.match_info['name']
  return web.Response(body=text.encode('utf-8'))

async def init(loop):
  app = web.Application(loop=loop)
  app.router.add_route('GET', '/', index)
  app.router.add_route('GET', '/hello/{name}', hello)
  srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
  print('Server started at http://127.0.0.1:8000...')
  return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()












