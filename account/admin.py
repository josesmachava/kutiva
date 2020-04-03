from django.contrib import admin
from .models import User, Student, Subscription

# Register your models here.




class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name']

admin.site.register(User, UserAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Student, StudentAdmin)




class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['expired_date']

admin.site.register(Subscription, SubscriptionAdmin)

