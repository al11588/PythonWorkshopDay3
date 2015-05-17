#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: alvinlawson
# @Date:   2015-05-13 22:28:41
# @Last Modified by:   alvinlawson
# @Last Modified time: 2015-05-13 22:29:09
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
]
