from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.utils.html import escape
from django.middleware.csrf import get_token
class displayContentView(View):
    def get(self,request,x):
        context={'number':x}
        return render(request,'life/display.html',context)
class additionContentView(View):
    def get(self,request,x,y):
        sum=x+y
        context={'numbers':[x,y],'sum':sum}
        return render(request,'life/add.html',context)
# Create your views here.

def dumpdata(place, data):
    retval=""
    if len(data)>0:
        retval="<p>Method: "+place+"data:<br/>\n"
        for key,value in data.items():
            retval+=escape(key)+"="+escape(value)+"</br>\n"
        retval+="</br\n></p>"
    return retval
def getForm(request):
    response="""<p>gET FoRm</P><form><label for="guess"><input type="text" name="guess" size="40" id="guess"></p><input type="submit"></form>"""
    response+=dumpdata('GET',request.GET)
    return HttpResponse(response)

def postForm(request):
    response="""<p>PoSt FoRm</P><form method="POST"><label for="guess"><input type="text" name="guess" size="40" id="guess"><input type="hidden" name="csrfmiddlewaretoken" value="__tok__"></p><input type="submit"></form>"""
    token=get_token(request)
    response=response.replace("__tok__",escape(token))
    response+=dumpdata('POST',request.POST)
    return HttpResponse(response)

class add(View):
    def get(self,request):
        msg=request.session.get('msg',False)
        if(msg): del(request.session['msg'])
        return render(request,'life/addform.html',{'message':msg}) 
    def post(self,request):
        if(request.POST["x"]!=request.POST["y"]):
            msg="UN-EQUAL!!!!!  :((("
        else:
            msg="EQUAL!!!! :)))"
        request.session['msg']=msg
        return redirect(request.path)