from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cms.models import *


# Create your views here.
def course(request):
    courses = Course.objects.all()
    return render(request, 'course/index.html', {'courses': courses})


def course_details(request, id):
    try:
        enrolled =  Enrolled.objects.filter(user=request.user)
        print(type(id))
        for i in enrolled:
            print(type(i.course.id))

        courses = Course.objects.all()
        course = Course.objects.get(id=id)
    except Course.DoesNotExist:
        raise Http404('This item does not exist')

    return render(request, 'course/details.html', {'course': course, 'courses': courses, 'enrolled':enrolled})



@login_required()
def classroom(request, id):
    try:
        course = Course.objects.get(id=id)
    except Course.DoesNotExist:
        raise Http404('This item does not exist')

    return render(request, 'course/classroom.html', {'course': course})



@login_required()
def user_courses(request):
    enrolled =  Enrolled.objects.filter(user=request.user)
    
    return render(request, 'course/paidCourse.html', {'enrolled':enrolled})

def add_course(request, id):
    try:
        course = Course.objects.get(id=id)
        enrolled = Enrolled.objects.create(course=course)
        enrolled.save()
        enrolled.user.add(request.user)

    except Course.DoesNotExist:
        raise Http404('This item does not exist')

    return redirect('index')
