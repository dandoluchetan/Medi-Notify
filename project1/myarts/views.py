from django.shortcuts import render
from myarts.models import article
from myarts.owner import OwnerDetailView,OwnerListView,OwnerUpdateView,OwnerCreateView,OwnerDeleteView
# Create your views here.
class artsList(OwnerListView):
    model=article
    template_name="myarts/myarts_list.html"

class artsDetail(OwnerDetailView):
    model=article
    template_name="myarts/myarts_detail.html"

class artsCreate(OwnerCreateView):
    model=article
    template_name="myarts/myarts_form.html"
    fields=['title','text']

class artsUpdate(OwnerUpdateView):
    model=article
    template_name="myarts/myarts_form.html"
    fields=['title','text']

class artsDelete(OwnerDeleteView):
    model=article
    template_name="myarts/myarts_confirm_delete.html"
