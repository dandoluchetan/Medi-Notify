from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils.html import escape
from django.views import View
import time
def home(request):
    response="""<html><head><title>Home</title><style>h1{color:darkred}</style></head><body><h1>WELCOME !!! THIS IS HOME PAGE</h1></body></html>"""
    return HttpResponse(response)
    #return HttpResponseRedirect('http://127.0.0.1:8000/main/redirect')

def funky(request):
    response="""<html><head><title>Happy Chetan</title></head><body><h1>This is FUnkY page.</h1></body></html>"""
    return HttpResponse(response)

def funkyWithGuess(request):
    response="""<html><head><title>Happy Chetan</title></head><body><h1>This is FUnkY page which Guesses """+request.GET['guess']+"""</h1></body></html>"""
    return HttpResponse(response)

def kgf(request,chapter):
    response="""<html><head><title>Happy Chetan</title></head><body><h1>This is KGF CH2 page which has collected """+escape(chapter)+""" crores</h1></body></html>"""
    return HttpResponse(response)

class chatHome(View):
    def get(self,request):
        return render(request,'project1/jsonfun.html')
        
def jsonfun(request):
    time.sleep(2)
    jsondata={"first":"first thing","second":"second thing"}
    return JsonResponse(jsondata)
    
class MainView(View):
    def get(self,request,guess):
        response="""<html><head><title>Happy Chetan</title></head><body><h1>This is a MainView pages under class MainView """+escape(guess)+"""</h1></body></html>"""
        return HttpResponse(response)