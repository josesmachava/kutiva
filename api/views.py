from django.shortcuts import render
from rest_framework import generics
from cms.models import Course
# from conference.models import Talk
from .serializers import CourseSerializer
# Create your views here.


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# class TalkList(generics.ListCreateAPIView):
#     queryset = Talk.objects.all()
#     serializer_class = TalkSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
