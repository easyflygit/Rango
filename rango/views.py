from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """Домашняя страница приложения Rango"""
    return HttpResponse("Rango says hey there partner!")
