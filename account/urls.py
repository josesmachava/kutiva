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
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

urlpatterns = [
    path('signin', views.signin, name="signin"),
    # path('signup', views.signup, name="signup"),
    path('signup/student', views.sudentsignup, name='student_sigin'),
    path('edit/<pk>', views.EditPerfile.as_view(), name="edit"),

    # path('logout', 'django.contrib.auth.views.logout',  {'next_page': '/successfully_logged_out/'}).
    path('', include('django.contrib.auth.urls')),

    # path('password_reset', auth_views.password_reset, name='password_reset'),
    # path('password_reset/done', auth_views.password_reset_done, name='password_reset_done'),
    # path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})',
    #     if settings.DEBUG:
    #         urlpatterns += static(settings.MEDIA_URL,
    #                               document_root=settings.MEDIA_ROOT) auth_views.password_reset_confirm, name='password_reset_confirm'),
    # path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),
]