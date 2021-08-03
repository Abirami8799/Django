from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello World!!')

def morning(request):
    return HttpResponse('Good Morning')

def night(request):
    return HttpResponse('Good night')