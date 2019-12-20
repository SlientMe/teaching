# -*- coding: utf-8 -*-
# @Time : 2019/12/20 12:58
# @Author : liuqi
# @FileName: urls.py
# @Software: PyCharm
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]