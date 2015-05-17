#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alvin Lawson
# @Date:   2015-05-17 12:26:23
# @Last Modified by:   Alvin Lawson
# @Last Modified time: 2015-05-17 12:38:41
from django.conf.urls import patterns, url
from bootstrap import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index')) #About page view