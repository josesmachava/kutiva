from django.http import Http404
from django.shortcuts import render
from cms.models import *


# Create your views here.
def course(request):
    courses = Course.objects.all()
    return render(request, 'course/index.html', {'courses': courses})


def course_details(request, id):
    try:
        course = Course.objects.get(id=id)
    except Course.DoesNotExist:
        raise Http404('This item does not exist')

    return render(request, 'course/details.html', {'course': course})


def classroom(request, id):
    try:
        course = Course.objects.get(id=id)
    except Course.DoesNotExist:
        raise Http404('This item does not exist')

    return render(request, 'course/classroom.html', {'course': course})


def user_courses(request):
    return render(request, 'course/user-courses.html')
