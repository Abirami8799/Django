from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.contrib import admin  

urlpatterns=[
    path('',views.home),
    path('submit',views.search),
    path('getword',views.getword)
]