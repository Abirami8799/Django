from django import urls
from django.urls import path
from . import views

urlpatterns=[
    path('',views.say_hello),
    path('home/',views.say_mrng),
    path('temp/',views.use_temp),
]
