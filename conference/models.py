from django.db import models


# Create your models here.
from account.models import Speaker
from kutiva import settings


class Talk(models.Model):
    author = models.OneToOneField(Speaker, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=100)
