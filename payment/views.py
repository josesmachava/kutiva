from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def Payment(request):
    return render(request, 'payment/payment.html')