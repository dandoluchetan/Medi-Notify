from django.urls import path
from . import views
urlpatterns=[
    path('questions/',views.viewQuestions.as_view(),name="viewQuestions"),
    path('questions/<int:q_no>/',views.viewChoices.as_view(),name="viewChoices"),
]