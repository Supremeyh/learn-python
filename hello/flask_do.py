#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# flask Web框架

# Python Web框架：flask； Django：全能型Web框架； web.py：一个小巧的Web框架； Bottle：和Flask类似的Web框架； Tornado：Facebook的开源异步Web框架

# 其实一个Web App，就是写一个WSGI的处理函数，针对每个HTTP请求进行响应。

# 用pip安装Flask：
# pip install flask

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  return '<h1>hello flask</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
  return '''
    <form action="/signin" method="post">
      <p><input name="username"></p>
      <p><input name="password" type="password"></p>
      <p><button type="submit">Sign In</button></p>
    </form>
  '''


@app.route('/signin', methods=['POST'])
def signin():
  if request.form['username'] == 'admin' and request.form['password'] == 'password':
    return '<h3>welcome admin, this is flask ! The Python micro framework for building web applications !</h3>'
  return '<h3>bad username or password</h3>'

if __name__ == '__main__':
  app.run()



#  运行flask_do.py， Flask自带的Server在端口5000上监听
# env FLASK_APP=flask_do.py flask run  # Running on http://127.0.0.1:5000/
# 打开浏览器，输入首页地址http://localhost:5000/
# 再输入地址http://localhost:5000/signin



# 使用模板
# 常见的模板有：Jinja2, Mako：用<% ... %>和${xxx}的一个模板；Cheetah：也是用<% ... %>和${xxx}的一个模板；
# Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。
# 在Jinja2模板中，我们用{{ name }}表示一个需要替换的变量。很多时候，还需要循环、条件判断等指令语句，在Jinja2中，用{% ... %}表示指令。
# 通过MVC，我们在Python代码中处理M：Model和C：Controller，而V：View是通过模板处理的，HTML代码全部放到模板里,就把Python代码和HTML代码最大限度地分离了。
# MVC：Model-View-Controller，中文名“模型-视图-控制器”。
# Python处理URL的函数就是C：Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等；
# 包含变量{{ name }}的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。
# Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据。如{ 'name': 'Michael' }

from flask import Flask, request, render_template

@app.route('/', methods=['GET', 'POST']) 
def home2():
  return render_template('home.html') # Flask通过render_template()函数来实现模板的渲染

# 安装模板 pip install jinja2
# 一定要把模板放到正确的templates目录下，templates和app.py在同级目录下。

