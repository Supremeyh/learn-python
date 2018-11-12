#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# WSGI：Web Server Gateway Interface
# WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。我们来看一个最简单的Web版本的“Hello, web!”：


def application(environ, start_response):
  start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
  body = '<h1>Hello,哈哈哈, %s! </h1>' % (environ['PATH_INFO'][1:] or 'web')
  return [body.encode('utf-8')]

# environ：一个包含所有HTTP请求信息的dict对象
# start_response：一个发送HTTP响应的函数。

