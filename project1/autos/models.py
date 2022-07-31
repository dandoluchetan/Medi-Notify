from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Make(models.Model):
    name=models.CharField(max_length=200,help_text='Enter a make(Ex: Ford) ',validators=[MinLengthValidator(2,'Please Enter 2 or more Characters for Make Name')])
    def __str__(self):
        return self.name

class Auto(models.Model):
    nickname=models.CharField(max_length=200,validators=[MinLengthValidator(2,'Please Enter 2 or more Characters for Nick Name')])
    mileage=models.PositiveIntegerField()
    comments=models.CharField(max_length=200)
    make_id=models.ForeignKey('Make',on_delete=models.CASCADE,null=False)

