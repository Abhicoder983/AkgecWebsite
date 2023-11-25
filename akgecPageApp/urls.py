from django.contrib import admin
from django.urls import path
from akgecPageApp import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('Career/', views.careers),
    
]
