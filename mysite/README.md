### 入门Django框架

#### 基础环境准备
1、安装 python

2、安装 Django
pip3 install Django
django-admin 查看是否安装成功

3、安装 PyCharm IDE

4、创建一个项目
django-admin startproject mysite

5、启动项目
python manage.py runserver

打开浏览器 http://127.0.0.1:8000/

6、创建应用
python manage.py startapp blog


#### hello django
视图、路由
```py
# blog/views.py
from django.http import HttpResponse
# Create your views here.
def hello(request):
  return HttpResponse('hello django!')


# blog/urls.py
from django.urls import path
from . import views

urlspatterns = [
  path('', views.hello, name='hello')
]


# mysite/urls.py
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  path('blog/', include('blog.urls'))
] 
```