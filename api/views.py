from django.shortcuts import render
from rest_framework import generics
from cms.models import Course
from .serializers import CourseSerializer

# Create your views here.


class CoursetList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class =  CourseSerializer
