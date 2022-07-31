from django.shortcuts import render
from django.http import HttpResponse

def func(request):
    return HttpResponse("Hi this is polls!!")
# Create your views here.
