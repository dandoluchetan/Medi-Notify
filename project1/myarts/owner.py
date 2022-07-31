from django.views.generic import CreateView,UpdateView,DeleteView,DetailView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
class OwnerListView(ListView):
    pass
class OwnerDetailView(DetailView):
    pass
class OwnerUpdateView(LoginRequiredMixin,UpdateView):
    def get_queryset(self,**kwargs):
        qs=super(OwnerUpdateView,self).get_queryset()
        return qs.filter(owner=self.request.user)
class OwnerCreateView(LoginRequiredMixin,CreateView):
    def form_valid(self,form):
        object=form.save(commit=False)
        object.owner=self.request.user
        object.save()
        return super(OwnerCreateView,self).form_valid(form)
class OwnerDeleteView(LoginRequiredMixin,DeleteView):
    def get_queryset(self,**kwargs):
        qs=super(OwnerDeleteView,self).get_queryset()
        return qs.filter(owner=self.request.user)