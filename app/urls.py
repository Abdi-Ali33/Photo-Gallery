from django.contrib import admin
from django.urls import include, path
from . import views

handler404 = 'app.views.handler404'

urlpatterns = [
    path('', views.index, name="index"),
    path('category/', views.category, name='category'),
    path('location/', views.location, name='location'),
    path('search', views.search, name='search')
]