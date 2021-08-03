from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse('<h1>Hello World!!!</h1>')

def say_mrng(request):
    return HttpResponse('Good Morning')
def use_temp(request):
    m={"data":['Abirami','Thenmozhi','kayalvizhi']}
    return render(request,'home.html', m)