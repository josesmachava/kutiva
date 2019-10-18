from datetime import timezone

from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField

from kutiva import settings


class Lesson(models.Model):
    name = models.CharField(max_length=1000)
    video = models.URLField()
    image = models.URLField()
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


class Course(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete='CASCADE', related_name='lesson')
    chapter = models.ManyToManyField(Chapter)
    is_active = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='course_cover')
    description = models.CharField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)


class Enrolled(models.Model):
    course = models.ForeignKey(Course, on_delete='CASCADE', blank=True, null=True)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, blank=True)


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
