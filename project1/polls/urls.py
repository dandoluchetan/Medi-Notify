from django.urls import path,include

from . import views
urlpatterns=[
    path('',views.func,name="func"),
    path('how-are-you/',include('app1.urls')),
]