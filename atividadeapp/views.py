from django.shortcuts import render
from .models import Especie, Category
# Create your views here.

def index(request):
    return render(request, 'index,html')

def Category(request):
    return render()

def Especie(request):
    return render()