# -*- coding: utf-8 -*-

from django.urls import path

from . import views
# 或者 import blog.views

urlspatterns = [
  path('', views.hello, name='hello')
]