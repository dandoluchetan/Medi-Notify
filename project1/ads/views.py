from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from ads.owner import OwnerListView,OwnerDetailView,OwnerDeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ads.models import Pic
from ads.forms import CreateForm
from django.urls import reverse_lazy
from django.http import HttpResponse
class adList(OwnerListView):
    model=Pic
    template_name="ads/list.html"
class adDetail(OwnerDetailView):
    model=Pic
    template_name="ads/detail.html"

class adCreate(LoginRequiredMixin,View):
    template_name="ads/form.html"
    success_url=reverse_lazy("ads:list")
    def get(self,request):
        form=CreateForm()
        ctx={'form':form}
        return render(request,"ads/form.html",ctx)
    def post(self,request):
        form=CreateForm(request.POST,request.FILES or None)
        if not form.is_valid():
            ctx={'form':form}
            return render(request,"ads/form.html",ctx)
        f=form.save(commit=False)#returns an instance where picture is extracted and converted to byte arr and is copied
        f.owner=self.request.user
        f.save()
        return redirect(self.success_url)


class adUpdate(LoginRequiredMixin,View):
    template_name="ads/form.html"
    success_url=reverse_lazy("ads:list")
    def get(self,request,pk):
        pic=get_object_or_404(Pic,id=pk,owner=self.request.user)
        form=CreateForm(instance=pic)
        ctx={'form':form}
        return render(request,"ads/form.html",ctx)
    def post(self,request,pk):
        pic=get_object_or_404(Pic,id=pk,owner=self.request.user)
        form=CreateForm(request.POST,request.FILES or None,instance=pic)
        if not form.is_valid():
            ctx={'form':form}
            return render(request,"ads/form.html",ctx)
        f=form.save(commit=False)#returns an instance where picture is extracted and converted to byte arr and is copied
        f.owner=self.request.user
        f.save()
        return redirect(self.success_url)

class adDelete(OwnerDeleteView):
    model=Pic
    template_name="ads/delete.html"
    success_url=reverse_lazy("ads:list")

def stream_file(request,pk):
    pic=get_object_or_404(Pic,id=pk)
    response=HttpResponse() 
    response['Content-Type']=pic.content_type
    response['Content-Length']=len(pic.picture)
    response.write(pic.picture)
    return response
