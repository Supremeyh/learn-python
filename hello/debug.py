# 错误处理、调试、测试

# 使用try...except捕获错误 
import logging
logging.basicConfig(level=logging.INFO) # 指定记录信息的级别，有debug，info，warning，error等几个级别


try:  # 运行一段可能会出错的代码
  print('try...')
  r = 10 / 0
  print('result: ', r)
except ValueError as e: # 捕获错误处理代码
  print('except: ', e)
  logging.exception(e) # logging记录错误
except ZeroDivisionError as e:
  print('except: ', e)
else: # 当没有错误发生
  print('no error')
finally:
  print('finally')

# 可以跨越多层调用
# 出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。
# 记录错误：Python内置的logging模块可以非常容易地记录错误信息：


# 五种调试方法： print()来辅助查看、 断言（assert）、 logging(是终极武器)、pdb、 pdb.set_trace()

# assert
# 凡是用print()来辅助查看出错的的地方，都可以用assert来替代
def foo(s):
  n = int(s)
  assert n != 0, 'n is zero!'  
  return 10 / n

def main():
  foo('0')

# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
# 启动Python解释器时可以用-O参数来关闭assert： python -O err.py, 关闭后，你可以把所有的assert语句当成pass来看。

# pdb
# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：
# err.py
s = '0'
n = int(s)
print(10 / n)
# 然后启动：
python -m pdb err.py
# 以参数-m pdb启动后，pdb定位到下一步要执行的代码, 输入命令l来查看代码,输入命令n可以单步执行代码,输入命令p 变量名来查看变量, 命令q结束调试，退出程序


# pdb.set_trace()
# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
import pdb

s = '0'
n = int(s)
pdb.set_trace # 在pdb.set_trace()暂停并进入pdb调试环境
print(10 / n)
# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：



# 单元测试, 用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。
# “测试驱动开发”（TDD：Test-Driven Development）
# 以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试用例。在将来修改的时候，可以极大程度地保证该模块行为仍然是正确的。
# 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。单元测试代码要非常简单。
# 如 mydict.py
class Dict(dict):
  def __init__(self,**kw):
    super().__init__(**kw)
  def __getattr__(self,key):
    try:
      return self[key]
    except KeyError:
      raise AttributeError(r "'Dic' object has no attribute '%s'" % key)
  def __setattr__(self, key, value):
    return self[key] = value
  
# 为了编写单元测试，我们需要引入Python自带的unittest模块
# mydict_test.py 测试代码
import unittest

from mydict import Dict

class TeatDict(unittest.TestCase): # 编写单元测试, 写测试类，从unittest.TestCase继承
  def test_init(self):  # 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
    d = Dict( a=1, b='test')
    self.assertEqual(d.a, 1)
    self.assertEqual(d.b, 'test')
    self.assertTrue(isinstance(d, dict))

  def test_key(self):
    d = Dict()
    d['key'] = 'value'
    self.assertEqual(d.key, 'value')
  
  def test_attr(self):
    d = Dict()
    d.key = 'value'
    self.assertTrue('key' in d)
    self.assertEqual(d['key'], 'value')
  
  def test_keyerror(self):
    d = Dict()
    with self.assertRaises(KeyError):
      value = d['empty']
  
  def test_attrerror(self):
    d = Dict()
    with self.assertRaises(AttributeError):
      value = d.empty()

  def setUp(self):
    print('setUp...')
  
  def tearDown(self):
    print('tearDown...')
  


# 运行单元测试:
# 测试代码末尾加上
if __name__ == '__main':
  unittest.main()
# 这样就可以把mydict_test.py当做正常的python脚本运行

# 在命令行通过参数-m unittest直接运行单元测试：
python -m unittest mydict_test.py
# 这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试


# setUp与tearDown
# 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。














