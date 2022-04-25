
from django.shortcuts import render, HttpResponse
from .models import Faculty,Document,Specialization,Type
# from datetime import datetime
# from  django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_fac(request):
    facs= Faculty.objects.all()
    context = {
        'facs': facs
    }
    print(context)
    return render(request, 'all_fac.html', context)


def add_type(request):
    facs=Type.objects.all()
    context = {
        'facs': facs
    }
    print(context)
    return render(request, 'add_type.html', context)

def add_doc(request):
    facs=Document.objects.all() 
    context = {
        'facs': facs
    }
    print(context)
    return render(request, 'add_doc.html', context)

def add_spc(request):
    facs=Specialization.objects.all()
    context = {
        'facs': facs
    }
    print(context)
    return render(request, 'add_spc.html', context)



