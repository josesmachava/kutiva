from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse
from cms.models import *

def index(request):
    courses = Course.objects.all()
    categories = Category.objects.all()
    return render(request, 'kutiva/index.html', {'courses':courses, 'categories':categories})





