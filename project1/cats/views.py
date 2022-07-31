from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from cats.models import breed,cat
from cats.forms import CatForm 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
class catList(View):
    def get(self,request):
        b_count=breed.objects.all().count()
        cats_list=cat.objects.all()
        ctx={'b_count':b_count,'cats_list':cats_list}
        return render(request,'cats/cats_list.html',ctx)

class catCreate(View):
    success_url=reverse_lazy("cats:cat-list")
    def get(self,request):
        #load empty form
        form1=CatForm()
        ctx={'form':form1}
        return render(request,'cats/cats_form.html',ctx)
    def post(self,request):
        #load form with submitted inputs
        form1=CatForm(request.POST)
        #check if inputs are valid or not
        if not form1.is_valid():
            ctx={'form':form1}
            return render(request,'cats/cats_form.html',ctx)
        #if valid then save
        form1.save()
        return redirect(self.success_url)

class catUpdate(View):
    success_url=reverse_lazy("cats:cat-list")
    def get(self,request,pk):
        c=get_object_or_404(cat,pk=pk)
        form1=CatForm(instance=c)
        ctx={'form':form1}
        return render(request,'cats/cats_form.html',ctx)
    def post(self,request,pk):
        c=get_object_or_404(cat,pk=pk)
        form1=CatForm(request.POST,instance=c)
        #check if inputs are valid or not
        if not form1.is_valid():
            ctx={'form':form1}
            return render(request,'cats/cats_form.html',ctx)
        #if valid then save
        form1.save()
        return redirect(self.success_url)

class catDelete(View):
    success_url=reverse_lazy("cats:cat-list")
    def get(self,request,pk):
        c=get_object_or_404(cat,pk=pk)
        ctx={'cat':c}
        return render(request,'cats/cats_confirm_delete.html',ctx)
    def post(self,request,pk):
        c=get_object_or_404(cat,pk=pk)
        c.delete()
        return redirect(self.success_url)

class breedList(View):
    template='cats/breed_list.html'
    def get(self,request):
        breed_list=breed.objects.all()
        context={'breed_list':breed_list}
        return render(request,self.template,context)

class breedCreate(LoginRequiredMixin,CreateView):
    model = breed
    fields = '__all__'
    success_url = reverse_lazy('cats:cat-list')
class breedUpdate(LoginRequiredMixin,UpdateView):
    model = breed
    fields = '__all__'
    success_url = reverse_lazy('cats:cat-list')
class breedDelete(LoginRequiredMixin,DeleteView):  
    model = breed
    fields = '__all__'
    success_url = reverse_lazy('cats:cat-list')