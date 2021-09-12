from django.shortcuts import render
from .models import Post


def createpost(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post=Post()
            post.title= request.POST.get('title')
            post.content= request.POST.get('content')
            post.save()
                
            return render(request, 'home.html')  

        else:
            return render(request,'home.html')