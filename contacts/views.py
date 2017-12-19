from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('homepage nav')


def list(request):
    return HttpResponse('listing')

def add(request):
    return HttpResponse('add contacts')
