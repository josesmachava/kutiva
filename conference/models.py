from django.db import models

# Create your models here.
from django.urls import reverse

from account.models import Speaker
from kutiva import settings


class Talk(models.Model):
    author = models.OneToOneField(Speaker, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(blank=True, )
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        self.title

    def get_absolute_url(self):
        return reverse('talk_edit', kwargs={'pk': self.pk})




