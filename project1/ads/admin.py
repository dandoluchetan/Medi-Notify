from django.contrib import admin
from ads.models import Pic
class Picadmin(admin.ModelAdmin):
    exclude=['picture','content_type']

admin.site.register(Pic,Picadmin)
