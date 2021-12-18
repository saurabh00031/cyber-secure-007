from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def blogx(request):
    return render(request,'blog.html')

def cyberinfo(request):
    return render(request,'cyberinfo.html')