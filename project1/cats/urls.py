from django.urls import path
from . import views
urlpatterns=[
    path('',views.catList.as_view(),name="cat-list"),
    path('main/create/',views.catCreate.as_view(),name="cat-create"),
    path('main/<int:pk>/update/',views.catUpdate.as_view(),name="cat-update"),
    path('main/<int:pk>/delete/',views.catDelete.as_view(),name="cat-delete"),
    path('lookup/create',views.breedCreate.as_view(),name="breed-create"),
    path('lookup/<int:pk>/update/',views.breedUpdate.as_view(),name="breed-update"),
    path('lookup/<int:pk>/delete/',views.breedDelete.as_view(),name="breed-delete"),
    path('lookup/',views.breedList.as_view(),name="breed-list"),
]