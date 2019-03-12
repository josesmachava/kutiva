from django.contrib import admin

# Register your models here.
from conference.models import Talk


class TalkAdmin(admin.ModelAdmin):
    list_display = ['title']



admin.site.register(Talk, TalkAdmin)
