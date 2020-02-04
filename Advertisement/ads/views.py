from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate,logout,login
from .models import Adv,Website    
from django.contrib.auth.models import User
import threading
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index_page(request):
    return render(request, 'ads/index.html')

@login_required
def wbs(request):
    c = Website.objects.all()
    c_length = len(c)
    context= {
        'c': c,
        'clen': c_length,
        }

    return render(request,'ads/website.html',context) 

@login_required
def advs(request):
    c = Adv.objects.all()
    c_length = len(c)
    context= {
        'c': c,
        'clen': c_length,
        }

    return render(request,'ads/ads.html',context) 

def register(request):
    if request.method=='POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        return HttpResponseRedirect('/login/')
    return render(request,'ads/register.html')


@login_required
def dashboard(request):
    username = request.user.username
    return render(request,'dashboard.html',{"user_name":username})

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
            return HttpResponseRedirect('/dashboard')
        else:
            print("login is false")
            return HttpResponseRedirect('/login/')

    return render(request,'ads/login.html')


def logout_view(request):  
    username = request.user.username  
    logout(request)
    return HttpResponseRedirect('/login/')