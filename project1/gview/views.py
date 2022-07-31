from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.list import ListView
from .models import Question,Choice
from django.http import Http404
# Create your views here.
class viewQuestions(ListView):
    model=Question
    template_name="gview/listQuestions.html"

class viewChoices(View):
    def get(self,request,q_no):
        str1=request.session.get('msg',False)
        if(str1): del(request.session['msg'])
        try:
            c=Choice.objects.filter(q_id=q_no)
            q=Question.objects.get(id=q_no)
            q_text=q.q_text
        except:
            raise Http404("Question does not exist")
        return render(request,"gview/listChoices.html",{'object_list':c.values(),'question':q_text,'message':str1})
    
    def post(self,request,q_no):
        c=Choice.objects.filter(id=int(request.POST["id"])).values()
        current_votes=int(c[0]["votes"])+1
        Choice.objects.filter(id=int(request.POST["id"])).update(votes=current_votes)  
        str1="Votes for "+c[0]["c_text"]+" are "+str(current_votes)
        request.session['msg']=str1
        return redirect(request.path)
        