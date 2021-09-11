from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.contrib import admin  


urlpatterns=[
    path('',views.travello),
]