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
from django.urls import path,include
from graphene_django.views import GraphQLView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('account/', include('account.urls')),
    path('graphql', GraphQLView.as_view(graphiql=True)),
    path('cms/', include('cms.urls')),
    path('payment/', include('payment.urls')),
    path("terms", views.terms, name="terms"),
    path('community/', include('community.urls')),
    path("price", views.price, name="price"),
    path("security", views.security, name="security"),
    path("policies", views.policies, name="policies"),
    path('api/', include('api.urls')), # new

    #path('cms/', include('cms.urls')),
   
]


handler404 = "kutiva.views.handler404"
handler500 = "kutiva.views.handler500"
