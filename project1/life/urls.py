from django.urls import path
from . import views
urlpatterns=[
    path('display/<int:x>',views.displayContentView.as_view(),name='displayFunc'),
    path('add-2/<int:x>+<int:y>',views.additionContentView.as_view(),name='add2Func'),
    #path('add-2/<int:x>/<int:y>',views.additionContentView.as_view(),name='add2Func'),
    path('addform/',views.add.as_view()),

    path('form1/',views.getForm),
    path('form2/',views.postForm),
]
