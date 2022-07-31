"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name="homePage"),
    path('chetan-Index/',include('app1.urls')),
    path('polls/',include('polls.urls')),

    path('funky/',views.funkyWithGuess),
    path('rocky/<slug:chapter>',views.kgf),
    path('main/<slug:guess>',views.MainView.as_view()),
    path('life/',include('life.urls')),

    path('gview/',include('gview.urls'),name="gview"),
    
    path('accounts/',include('django.contrib.auth.urls')),
    path('authz/',include('authz.urls')),
    
    path('autos/',include(('autos.urls','autos'),namespace="autos")),
    path('cats/',include(('cats.urls','cats'),namespace="cats")),
    path('myarts/',include(('myarts.urls','myarts'),namespace="myarts")),
    path('ads/',include(('ads.urls','ads'),namespace="ads")),

    path('chat/home/',views.chatHome.as_view()),
    path('chat/home/jsonfun/',views.jsonfun),
    path('admin/', admin.site.urls),
]
