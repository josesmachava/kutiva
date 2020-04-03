from datetime import timezone

from django.db import models
from django.utils import timezone
import datetime
from dateutil.relativedelta import relativedelta
from kutiva import settings


class Lesson(models.Model):
    name = models.CharField(max_length=1000)
    video = models.URLField()
    # image = S3DirectField(dest='primary_destination', blank=True)
    image = models.FileField()
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Subcategory(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=1000)
    subcategory = models.ForeignKey(Subcategory, on_delete='CASCADE', blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Chapter(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField()
    lessons = models.ManyToManyField(Lesson)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)


class SubscriptionType(models.Model):
    name = models.CharField(max_length=1000)
    month = models.IntegerField(default=1, blank=False)
    price = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)

    def get_month(self):
        return self.month


class Subscription(models.Model):
    subscription_type =  models.ForeignKey(SubscriptionType, on_delete='CASCADE', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    expired_date = models.DateField(default=datetime.date.today() + relativedelta(months=SubscriptionType._meta.get_field('month').get_default()))

    def __str__(self):
        return str(self.expired_date)



class Course(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete='CASCADE', related_name='lesson')
    chapter = models.ManyToManyField(Chapter)
    is_active = models.BooleanField(default=False)
    image = models.FileField()
    description = models.CharField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)


class Testimonial(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    testimonial = models.TextField()

    def __str__(self):
        return str(self.user)


class SocialNetwork(models.Model):
    name = models.CharField(max_length=1000)
    url = models.URLField()
    icon = models.FileField(upload_to='icons')

    def __str__(self):
        return str(self.name)


class Partner(models.Model):
    name = models.CharField(max_length=1000)
    image = models.URLField()
    url = models.URLField()

    def __str__(self):
        return str(self.name)
