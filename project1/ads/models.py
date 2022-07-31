from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
class Pic(models.Model):
    title=models.CharField(max_length=128,validators=[MinLengthValidator(2,'Title must be greater than 2 characters')])
    text=models.TextField()
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #picture
    picture=models.BinaryField(null=True,blank=True,editable=True)
    content_type=models.CharField(max_length=256,null=True,blank=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

