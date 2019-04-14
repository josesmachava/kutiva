from django.http import Http404
from django.shortcuts import render
from cms.models import *
# Create your views here.
from cms.models import Course


def dashboard(request):
    return render(request, "cms/speaker.html")



