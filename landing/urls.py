# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 22:39:04 2020

@author: rolly
"""

from django.urls import path, include

from . import views

app_name='landing'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('token/', views.token, name='token'),
    path('profile/', views.profile, name='profile'),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('', views.index),

    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]