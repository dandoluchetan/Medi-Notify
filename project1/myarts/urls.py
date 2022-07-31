from django.urls import path
from django.urls import reverse_lazy
from . import views
urlpatterns=[
    path('',views.artsList.as_view(),name='list'),
    path('article/create/',views.artsCreate.as_view(success_url=reverse_lazy('myarts:list')),name='create'),
    path('article/<int:pk>/update/',views.artsUpdate.as_view(success_url=reverse_lazy('myarts:list')),name='update'),
    path('article/<int:pk>/delete/',views.artsDelete.as_view(success_url=reverse_lazy('myarts:list')),name='delete'),
    path('article/<int:pk>',views.artsDetail.as_view(),name='detail'),
]