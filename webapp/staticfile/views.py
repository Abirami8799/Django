from staticfile.models import Destination
from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def travello(request):

    dest1= Destination()
    
    dest1.name= 'TamilNadu'
    dest1.price= 750
    dest1.desc= 'Shore Temple, Mahabalipuram'
    dest1.img='destination_1.jpg'


    dest2= Destination()
    dest2.name= 'Kerala'
    dest2.price= 700
    dest2.desc= ' Edakkal Caves, Wayanad'
    dest2.img='destination_2.jpg'

    dest3= Destination()
    dest3.name= ' Karnataka'
    dest3.price= 800
    dest3.desc= 'Mysore Palace, Mysore'
    dest3.img='destination_3.jpg'

    dests=[dest1,dest2, dest3]

    return render(request,'index.html',{'dests':dests})






