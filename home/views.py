from django.http import HttpResponse
from django.shortcuts import render
from .models import TestMeters,Datos
from subprocess import call

import requests
import sys

# Create your views here.
def homeView(request):
    return render(request,'home/index.html')

#def abrirAPI(request):
 #   return render(request,'home/index.html')

def abrirAPI(request):
    call(['python', 'prueba.py'])
    return render(request,'home/index.html')

def tabla(request):
    #datos = TestMeters.objects.all()
    datos = Datos.objects.using('db2').all()
    return render(request, 'home/tablacss.html', {'datos': datos})
