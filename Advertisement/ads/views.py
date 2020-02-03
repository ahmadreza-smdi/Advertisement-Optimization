from django.shortcuts import render
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
from .models import Adv,Website    
from django.contrib.auth.models import User
import threading
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Create your views here.

def index_page(request):
    return render(request, 'ads/index.html')


def register(request):
    return render(request,'ads/register.html')


def logged_in(request):
    if request.user.is_authenticated:
        return True
    else:
        return False

def loginn(request):
    if request.method == 'POST':
        username=request.POST.get('username','')
        print("username:",username)
        password=request.POST.get("password",'')
        print("password",password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            print("login is true")
            return HttpResponseRedirect('/1')
        else:
            print("login is false")
            return HttpResponseRedirect('/login/')

    return render(request,'ads/login.html')
