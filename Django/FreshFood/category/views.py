from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def index (name='index'):
    return HttpResponse("category")
# Create your views here.
