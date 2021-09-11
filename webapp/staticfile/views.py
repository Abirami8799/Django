from staticfile.models import Destination
from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def travello(request):

    dest1= Destination()
    
    dest1.name= 'chennai'
    dest1.price= 800
    dest1.desc= 'TamilNadu captial'

    return render(request,'index.html',{'dest1':dest1})






