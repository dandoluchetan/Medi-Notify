from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
class OwnerListView(ListView):
    pass
class OwnerDetailView(DetailView):
    pass
# class OwnerCreateView(LoginRequiredMixin,CreateView):
#     def form_valid(self,form):
#         f=form.save(commit=False)
#         f.owner=self.request.user
#         f.save()
#         return super(OwnerCreateView,self).form_valid(form)
        
# class OwnerUpdateView(LoginRequiredMixin,UpdateView):
#     def get_queryset(self,**kwargs):
#         qs=super(OwnerUpdateView,self).get_queryset()
#         return qs.filter(owner=self.request.user)

class OwnerDeleteView(LoginRequiredMixin,DeleteView):
    def get_queryset(self):
        print('delete get_queryset called')
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)

