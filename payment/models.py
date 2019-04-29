from datetime import timezone


from django.utils import timezone
from django.db import models
from kutiva import settings
# Create your models here.

class payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number_sender = models.CharField(max_length=15)
    mount = models.DecimalField(max_digits=6, decimal_places=2)
    created_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    last_day = models.DateTimeField()