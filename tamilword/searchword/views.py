from abc import abstractproperty
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files import File
import os
import tamil
from tamil.utf8 import get_letters, get_letters_length, get_words


def home(request):
    return render(request,'home.html')


def search(request):
    if request.POST.get('res'):
        value=int(request.POST['val'])
        request.session['name']=value
        return render(request,'base.html',{'data':range(2,value+1)})

def getword(request):
    if request.POST.get('input'):
        value= request.session['name']
        l=[]
        for i in range(1,value+1):
            x=request.POST[f'box{i}']
            l.append(x)
        if bool(l[0]):
            s=[]
            n=''.join(map(str,l))
            for root, dirs, files in os.walk("C:/Users/codiislap10/Documents/", topdown=False):
                for name in dirs:
                     if name == "len_"+str(value):
                         a=os.path.join(root,name)
            for root, dirs, files in os.walk(a):
                for val in files:
                    if val.startswith(n[0]):
                        b=os.path.join(root,val)
            file1=open(b,encoding="utf-8")
            lines=file1.read()
            word=get_words(lines)


            r=get_letters_length(n)

            for each in word:  
                 m=get_letters(each)
                 if each.startswith(l[0]) and each.endswith(l[value-1]):   
                      y=[m.index(j) for i,j in zip(l,m) if i==j]
                      if len(y)==r:
                         s.append(''.join(map(str,m)))

            m={"data":s} 
            return render(request,'result.html',m)
        else:
            m={"name":"you must enter first letter"}
            return render(request,'result.html',m)
    
