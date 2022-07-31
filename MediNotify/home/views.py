from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from home.forms import SignUpForm,LoginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .owner import OwnerCreateView,OwnerListView,OwnerUpdateView,OwnerDeleteView
from django.views.generic.list import ListView
from django.contrib.auth import logout
from .forms import MedicineDetailsForm, ContactsForm
from .models import MedicineDetails,Contacts
from .owner import OwnerListView
# Create your views here.
class SignUp(View):
    def get(self,request):
        register_form=SignUpForm()
        ctx={'form':register_form}
        return render(request,'home/register_form.html',ctx)
    def post(self,request):
        form=SignUpForm(request.POST)
        if not form.is_valid():
            ctx={'form':form}
            return render(request,"home/register_form.html",ctx)
        form.save()
        return redirect("home:login")

class LoginView(auth_views.LoginView):
    form_class=LoginForm
    template_name="registration/login.html"
    success_url=reverse_lazy("home:homepage")

class HomePage(View):
    def get(self,request):
        return render(request,"home/postlogin/about.html")

class TodayPage(View):
    pass

class YourMedicines(OwnerListView):
    model=MedicineDetails
    template_name='home/postlogin/your_medicines_list.html'
    context_object_name='medicines_list'
    

class AddMedicine(LoginRequiredMixin,View):
    success_url=reverse_lazy('home:homepage')
    def get(self,request):
        form=MedicineDetailsForm()
        ctx={'form':form}
        return render(request,'home/postlogin/your_medicines_add_form.html',ctx)
    def post(self,request):
        form=MedicineDetailsForm(request.POST)
        if not form.is_valid():
            ctx={'form':form}
            return render(request,'home/postlogin/your_medicines_add_form.html',ctx)
        f=form.save(commit=False)
        f.user=self.request.user
        f.save()
        return redirect(self.success_url)

class UpdateMedicine(LoginRequiredMixin,View):
    success_url=reverse_lazy('home:homepage')
    def get(self,request,pk):
        md=get_object_or_404(MedicineDetails,pk=pk)
        form=MedicineDetails(instance=md)
        ctx={'form':form}
        return render(request,'home/postlogin/your_medicines_add_form.html',ctx)
    def post(self,request,pk):
        md=get_object_or_404(MedicineDetails,pk=pk)
        form=MedicineDetails(request.POST,instance=md)
        if not form.is_valid():
            ctx={'form':form}
            return render(request,'home/postlogin/your_medicines_add_form.html',ctx)
        f=form.save(commit=False)
        f.user=self.request.user
        f.save()
        return redirect(self.success_url)

class DeleteMedicine(LoginRequiredMixin,View):
    success_url=reverse_lazy('home:homepage')
    def get(self,request,pk):
        md=get_object_or_404(MedicineDetails,pk=pk)
        ctx={'medicine':md}
        return render(request,'home/postlogin/your_medicines_confirm_delete.html',ctx)
    def post(self,request,pk):
        c=get_object_or_404(cat,pk=pk)
        c.delete()
        return redirect(self.success_url)

class YourContacts(View):
    def get(self,request):
        form=ContactsForm()
        ctx={'form':form}
        return render(request,'home/postlogin/your_contacts_add_form.html',ctx)

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("home:homepage"))
