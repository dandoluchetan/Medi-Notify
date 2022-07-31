from django.urls import path
from . import views
urlpatterns=[
    path('',views.adList.as_view(),name="list"),
    path('pics/<int:pk>',views.adDetail.as_view(),name="detail"),
    path('pics/create/',views.adCreate.as_view(),name="create"),
    path('pics/<int:pk>/update/',views.adUpdate.as_view(),name="update"),
    path('pics/<int:pk>/delete/',views.adDelete.as_view(),name="delete"),
    path('pics/picture/<int:pk>/',views.stream_file,name="picture")
]