from email.policy import default
from django.db import models
from pyexpat import model

# Create your models here.
class TaskModel(models.Model):
    task = models.CharField(max_length=100)
    isComplete = models.BooleanField(default=False)
    date = models.DateTimeField (auto_now_add= True) 

    def __str__(self) -> str:
        return self.task 