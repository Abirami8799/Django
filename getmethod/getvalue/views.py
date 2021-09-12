from django.shortcuts import render

from .models import Post



def show(request):
    students = Post.objects.all()
    return render(request,"show.html",{'student':students})
