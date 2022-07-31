from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Contacts,MedicineDetails
admin.site.register(get_user_model())
admin.site.register(Contacts)
admin.site.register(MedicineDetails)
# Register your models here.
