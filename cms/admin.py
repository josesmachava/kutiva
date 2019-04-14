from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Chapter)
admin.site.register(Lesson)
admin.site.register(Enrolled)