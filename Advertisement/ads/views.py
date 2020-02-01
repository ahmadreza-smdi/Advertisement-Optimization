from django.shortcuts import render

# Create your views here.

def login_page(request):
    return render(request, 'ads/index.html')