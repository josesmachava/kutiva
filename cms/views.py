from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def course(request):
    courses = Course.objects.all()
    return render(request, 'course/index.html', {'courses': courses})


def course_details(request, id):
    try:
        if request.user.is_authenticated:
            courses = Course.objects.all()
            course = Course.objects.get(id=id)

        courses = Course.objects.all()
        course = Course.objects.get(id=id)
    except Course.DoesNotExist:
        raise Http404('This item does not exist')

    return render(request, 'course/details.html', {'course': course, 'courses': courses})


@login_required()
def classroom(request, id):
    if request.user.is_student == False:
        return render(request, 'course/payment.html')

    elif request.user.is_student == False or request.user.student.subscription.expired_date == datetime.date.today():
        return render(request, 'course/payment.html')

    elif request.user.student.subscription.expired_date == datetime.date.today():
        return render(request, 'course/payment.html')


    else:

        try:
            course = Course.objects.get(id=id)
        except Course.DoesNotExist:
            raise Http404('This item does not exist')

        return render(request, 'course/classroom.html', {'course': course})


@login_required()
def watch(request, course_id, lesson_id=1):
    if request.user.student.is_student == False:
        return render(request, 'course/payment.html')

    elif request.user.student.is_student == False or request.user.student.subscription.expired_date == datetime.date.today():
        return render(request, 'course/payment.html')

    elif request.user.student.subscription.expired_date == datetime.date.today():
        return render(request, 'course/payment.html')

    else:

        try:
            course = Course.objects.get(id=course_id)
            lesson = Lesson.objects.get(id=lesson_id)
        except Course.DoesNotExist:
            raise Http404('This item does not exist')

        return render(request, 'course/watch.html', {'course': course, 'lesson': lesson})


@login_required()
def payment(request):
    return render(request, 'course/payment.html')


@login_required()
def user_courses(request):
    enrolled = Enrolled.objects.filter(user=request.user)

    return render(request, 'course/paidCourse.html', {'enrolled': enrolled})


def add_course(request, id):
    try:
        course = Course.objects.get(id=id)
        enrolled = Enrolled.objects.create(course=course)
        enrolled.save()
        enrolled.user.add(request.user)

    except Course.DoesNotExist:
        raise Http404('This item does not exist')

    return redirect('mycourses')
