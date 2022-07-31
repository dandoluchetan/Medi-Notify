from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from autos.models import Auto, Make
from autos.forms import MakeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
class MainView(LoginRequiredMixin,View):
    template='autos/auto_list.html'
    def get(self,request):
        make_count=Make.objects.all().count()
        auto_list=Auto.objects.all()
        context={'make_count':make_count,'auto_list':auto_list}
        return render(request,self.template,context)

class MakeView(LoginRequiredMixin,View):
    template='autos/make_list.html'
    def get(self,request):
        make_list=Make.objects.all()
        context={'make_list':make_list}
        return render(request,self.template,context)

class MakeCreate(LoginRequiredMixin,View):
    template='autos/make_form.html'
    success_url=reverse_lazy("autos:all")

    def get(self,request):
        form=MakeForm()
        context={'form':form}
        return render(request,self.template,context)
    def post(self,request):
        form=MakeForm(request.POST)
        if not form.is_valid():
            context={'form':form}
            return render(request,self.template,context)#returning without redirect get bevause no changes in data were made.
        form.save()
        return redirect(self.success_url)

class MakeUpdate(LoginRequiredMixin,View):
    template="autos/make_form.html"
    success_url=reverse_lazy("autos:all")

    def get(self,request,pk):
        make=get_object_or_404(Make,pk=pk)
        form=MakeForm(instance=make)
        context={'form':form}
        return render(request,self.template,context)
    def post(self,request,pk):
        make=get_object_or_404(Make,pk=pk)
        form=MakeForm(request.POST,instance=make)
        if not form.is_valid():
            context={'form:':form}
            return render(request,self.template,context)
        form.save()
        return redirect(self.success_url)

class MakeDelete(LoginRequiredMixin,View):
    template="autos/make_confirm_delete.html"
    success_url=reverse_lazy("autos:all")

    def get(self,request,pk):
        make=get_object_or_404(Make,pk=pk)
        form=MakeForm(instance=make)
        context={'make':make}
        return render(request,self.template,context)
    def post(self,request,pk):
        make=get_object_or_404(Make,pk=pk)
        make.delete()
        return redirect(self.success_url)

class AutoCreate(LoginRequiredMixin,CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
class AutoUpdate(LoginRequiredMixin,UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
class AutoDelete(LoginRequiredMixin,DeleteView):  
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')