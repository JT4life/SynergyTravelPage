from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('', views.home,name="Home"),
    path('home/', views.home,name="Home"),
    path('add', views.add, name="add")
]