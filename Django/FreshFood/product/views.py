from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is product")    

def firstProduct(request):
    return HttpResponse("Frist product")
