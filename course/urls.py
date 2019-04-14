"""kutiva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.course, name="course"),
    path('details/<id>', views.course_details, name='details'),
    path('classroom/<id>', views.classroom, name='classroom'),
    path('mycourses', views.user_courses, name="mycourses"),
    path('<id>', views.add_course, name='add_course'),

]
