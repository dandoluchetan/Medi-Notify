from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.LoginView.as_view(),name='login'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('',views.HomePage.as_view(),name='homepage'),
    path('logout/', views.LogoutView, name='logout'),

    path('medicines-for-today/',views.TodayPage.as_view(),name='today'),
    path('your-medicines/',views.YourMedicines.as_view(),name='yourMedicines'),
    path('your-medicines/add/',views.AddMedicine.as_view(),name='addYourMedicine'),
    path('your-medicines/<int:pk>/update/',views.UpdateMedicine.as_view(),name='updateYourMedicine'),
    path('your-medicines/<int:pk>/delete/',views.DeleteMedicine.as_view(),name='DeleteYourMedicine'),
    path('your-contacts/',views.YourContacts.as_view(),name='yourContacts')
]