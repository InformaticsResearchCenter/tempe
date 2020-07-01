# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 22:39:04 2020

@author: rolly
"""

from django.urls import path

from . import views

app_name='landing'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]