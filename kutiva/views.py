from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse
from cms.models import *

def index(request):
    courses = Course.objects.all()
    partners = Partner.objects.all()
    categories = Category.objects.all()

    return render(request, 'kutiva/index.html', {'courses':courses, 'categories':categories, 'partners':partners})






def security(request):
    return render(request, "about/security.html")

def terms(request):
    return render(request, "about/terms.html")

def policies(request):
    return render(request, "about/policies.html")


def error_404_view(request):
    return render(request,'error/404.html')


def error_500_view(request):
    return render(request,'error/500.html')