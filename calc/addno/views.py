from django.shortcuts import render
from django.http import HttpResponse, request
from django.forms import forms
from django.core.files import File

def home(request):
    return render(request,'calc.html')

def cal(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    if request.POST.get('add'):
        res=val1+val2
    elif request.POST.get('sub'):
        res=val1-val2
    elif request.POST.get('mul'):
        res=val1*val2
    elif request.POST.get('div'):
        res=val1/val2
      
    return render(request,'result.html',{'data':res})
    

