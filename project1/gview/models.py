from django.db import models

class Question(models.Model):
    q_text=models.CharField(max_length=200)
class Choice(models.Model):
    c_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    q_id=models.ForeignKey(Question,on_delete=models.CASCADE)

# Create your models here.
