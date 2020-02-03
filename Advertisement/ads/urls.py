from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('',views.index_page),
    url(r'^login/$',views.loginn),
    url(r'^registration/$',views.register),
    url(r'^dashboard/$',views.dashboard),
    url(r'^dashboard/logout/$',views.logout_view),


]
