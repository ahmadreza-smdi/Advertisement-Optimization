# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate,logout,login
from .models import Adv,Website    
from django.contrib.auth.models import User
import threading
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
import hazm
import numpy as np
import matplotlib.pyplot as plt
import fasttext
import fasttext.util
from sklearn.cluster import KMeans

model = fasttext.load_model("cc.fa.300.bin.bin")
fasttext.util.reduce_model(model, 100)
normalizer = hazm.Normalizer()
stemmer = hazm.Stemmer()
lemmatizer = hazm.Lemmatizer()
tagger = hazm.POSTagger(model='resources/postagger.model')

def text2vec(text):
    text = normalizer.normalize(text)
    tagged_words = tagger.tag(hazm.word_tokenize(text))
    words_vector = []
    for tagged in tagged_words:
        if tagged[1] == 'N' or tagged[1] == 'Ne':
            word = lemmatizer.lemmatize(tagged[0])
            if word == 'لپ':
                word = 'لپتاپ'
            if word == 'تاپ':
                continue
            words_vector.append(model.get_word_vector(word))

    return np.mean(np.array(words_vector), axis=0)


def clustering(descriptions):
    descriptions_vectors = []
    for text in descriptions:
        descriptions_vectors.append(text2vec(text))

    descriptions_vectors = np.array(descriptions_vectors)

    kmeans = KMeans(n_clusters=12, random_state=0).fit(descriptions_vectors)

    return kmeans


def predict_related_sites(text, sites):
    global kmeans
    cluster = kmeans.predict(text2vec(text))
    related_points = np.argwhere(kmeans.labels_ == cluster)
    related_sites = []
    for i in related_points:
        related_sites.append(sites[i])

    return related_sites


queries = Website.objects.all()
descriptions = []
for query in queries:
    descriptions.append(query.des)

kmeans = clustering(descriptions)



# Create your views here.

def index_page(request):
    q = False
    if request.user.is_authenticated:
        q= True

    context={
        'q':q
    }

    # with open('/media/ahmadreza/48AC8787AC876E6E/Project/Advertise/Advertisement/ads/sites.txt') as f:
    #     sites = [line.rstrip() for line in f]

    # with open('/media/ahmadreza/48AC8787AC876E6E/Project/Advertise/Advertisement/ads/descriptions.txt') as f:
    #     descriptions = [line.rstrip() for line in f]
    
    # userid = request.user

    # for i in range(len(sites)):
    #     website = Website(url=sites[i],des = descriptions[i],user=userid)
    #     website.save()
    return render(request, 'ads/index.html',context)

@login_required(login_url='/login/')
def wbs(request):
    c = Website.objects.all()
    c_length = len(c)
    context= {
        'c': c,
        'clen': c_length,
        }

    return render(request,'ads/website.html',context) 

@login_required(login_url='/login/')

def advs(request):
    c = Adv.objects.all()
    c_length = len(c)
    context= {
        'c': c,
        'clen': c_length,
        }

    return render(request,'ads/ads.html',context) 

@login_required(login_url='/login/')
def regweb(request):
    if request.method=='POST': 
        userid = request.user
        url = request.POST.get('url')
        des = request.POST.get('des')
        website = Website(url=url,des = des,user=userid)
        website.save()

        global kmeans
        queries = Website.objects.all()
        descriptions = []
        for query in queries:
            descriptions.append(query.des)
        kmeans = clustering(descriptions)


        return HttpResponseRedirect('/dashboard/websites/')
     
    return render(request,'ads/AddWebsite.html')

@login_required(login_url='/login/')
def ad(request):
    p = False
    context= {
        'p': p,
        }
    if request.method=='POST':
        text = request.POST.get('Add')
        context['p'] = True 
        queries = Website.objects.all()
        sites = []
        for query in queries:
            sites.append(query.url)

        related_sites = predict_related_sites(text, sites)      
        Related_website_url = ''

        for site in related_sites:
            Related_website_url += site + '\n'

        userid = request.user
        Adv = Adv(context=text,Related_website_url = Related_website_url,user=userid)
        Adv.save()
    


              







        return render(request,'ads/AddAd.html',context)

        
    return render(request,'ads/AddAd.html',context)


def register(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request,'dashboard.html',{"user_name":username})
    else:
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


@login_required(login_url='/login/')
def dashboard(request):
    username = request.user.username
    return render(request,'dashboard.html',{"user_name":username})

def logged_in(request):
    if request.user.is_authenticated:
        return True
    else:
        return False

def loginn(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request,'dashboard.html',{"user_name":username})
    else:
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