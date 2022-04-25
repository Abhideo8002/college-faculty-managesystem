
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('all_fac', views.all_fac, name ='all_fac'),
    path('add_type', views.add_type, name ='add_type'),
    path('add_doc', views.add_doc, name ='add_doc'),
    path('add_spc', views.add_spc, name ='add_spc'),
]
    