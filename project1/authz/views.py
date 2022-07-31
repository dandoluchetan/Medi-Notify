from django.shortcuts import render
from django.views import View
# Create your views here.
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse
class dumpPython(View):
    def get(self,request):
        resp=''
        resp+='User data in python'+'<br>'+'<br>'
        resp+='url to login:'+reverse('login')+'<br>'
        resp+='url to logout:'+reverse_lazy('logout')
        return HttpResponse(resp)

