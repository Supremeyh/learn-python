# 错误处理、调试、测试

# 使用try...except捕获错误 
import logging

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

