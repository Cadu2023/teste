from django.urls import path
from .views import Especie, Category

urlpatterns = [
path('', Especie,name='Especie'),
path('', Category, name='Category')
]