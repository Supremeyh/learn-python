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
    return '<h3>hello admin </h3>'
  return '<h3>bad username or password</h3>'

if __name__ == '__main__':
  app.run()



#  运行flask_do.py， Flask自带的Server在端口5000上监听
# env FLASK_APP=flask_do.py flask run  # Running on http://127.0.0.1:5000/
# 打开浏览器，输入首页地址http://localhost:5000/：