from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

def say_hello(request):
    return HttpResponse('The date is ' +str(date.today())+'!!')
