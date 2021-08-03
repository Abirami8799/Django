from django.shortcuts import render
from django.http import HttpResponse, request
from django.forms import forms
from django.core.files import File

def home(request):
    return render(request,'base.html')

def cal(request):
    val=int(request.POST['num1'])
    if request.POST.get('res'):
       l=[]
       f = open('C:/Users/codiislap10/Documents/abi.txt', 'r')
       contents =File(f)
       words=[line.strip() for line in contents]
       for each in words:
           if val == len(each):
                l.append(each)
    m={"data":l}
    return render(request,'result.html',m)
    


