# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 22:39:04 2020

@author: rolly
"""

from django.urls import path

from . import views

app_name='landing'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]