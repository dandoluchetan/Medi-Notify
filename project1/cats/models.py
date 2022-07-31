from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class breed(models.Model):
    breedName=models.CharField(max_length=200,help_text='Enter an item',validators=[MinLengthValidator(2,'Name of the cat breed should be more than 2')])
    def __str__(self):
        return self.breedName
class cat(models.Model):
    Nickname=models.CharField(max_length=200)
    Weight=models.PositiveIntegerField()
    Foods=models.CharField(max_length=200)
    Breed=models.ForeignKey('breed',on_delete=models.CASCADE,null=False)