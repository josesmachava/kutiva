# from django.db import models
# from django.utils.datetime_safe import datetime
#
#
# class Lesson(models.Model):
#     name = models.CharField(max_length=1000)
#     video = models.FileField()
#
#     def __str__(self):
#         return self.name
#
#
# class Subcategory(models.Model):
#     name = models.CharField(max_length=1000)
#
#     def __str__(self):
#         return self.name
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=1000)
#     subcategory = models.ForeignKey(Subcategory, on_delete='CASCADE', blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Chapter(models.Model):
#     name = models.CharField(max_length=1000)
#     description = models.TextField()
#     lessons = models.ManyToManyField(Lesson)
#
#     def __str__(self):
#         return self.name
#
#
# class Course(models.Model):
#     name = models.CharField(max_length=1000)
#     category = models.ForeignKey(Category, on_delete='CASCADE', related_name='lesson')
#     cover = models.ImageField
#     description = models.CharField(max_length=1000)
#     lesson = models.ManyToOneRel(Chapter, on_delete='CASCADE', related_name='chapter')
#
#     def __str__(self):
#         return self.name
