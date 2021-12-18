from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('blog',views.blogx,name="blog"),
    path('cyberinfo',views.cyberinfo,name="cyberinfo"),
]
