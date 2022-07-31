from django.urls import path
from . import views
urlpatterns=[
    path('',views.MainView.as_view(),name="all"),
    path('make/',views.MakeView.as_view(),name="make-list"),
    path('make/create/',views.MakeCreate.as_view(),name="make-create"),
    path('make/<int:pk>/update/',views.MakeUpdate.as_view(),name="make-update"),
    path('make/<int:pk>/delete/',views.MakeDelete.as_view(),name="make-delete"),
    path('auto/create/',views.AutoCreate.as_view(),name="auto-create"),
    path('auto/<int:pk>/update/',views.AutoUpdate.as_view(),name="auto-update"),
    path('auto/<int:pk>/delete/',views.AutoDelete.as_view(),name="auto-delete"),
]