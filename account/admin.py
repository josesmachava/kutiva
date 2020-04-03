from django.contrib import admin

from cms.models import SubscriptionType
from .models import User, Student, Subscription

# Register your models here.




class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name']

admin.site.register(User, UserAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Student, StudentAdmin)




class SubscriptionTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(SubscriptionType, SubscriptionTypeAdmin)




class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['expired_date']

admin.site.register(Subscription, SubscriptionAdmin)

