from django.db import models
from django.forms import ModelForm


class Instructor(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    description = models.TextField()


class Event(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    location = models.CharField(max_length=50)
    duration = models.IntegerField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    start_date = models.DateField()
    end_date = models.DateField()


class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()

