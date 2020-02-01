from django.shortcuts import render

# Create your views here.

def index_page(request):
    return render(request, 'ads/index.html')

def loginn(request):
    return render(request,'ads/login.html')

def register(request):
    return render(request,'ads/register.html')