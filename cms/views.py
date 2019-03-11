from django.http import Http404
from django.shortcuts import render

# Create your views here.
from cms.models import Course


def dashboard(request):
    return render(request, "cms/index.html")


