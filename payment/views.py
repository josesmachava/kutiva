import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime 
from django.utils.timezone import localtime, now
from datetime import timedelta
import calendar
from django.contrib.auth.decorators import login_required
from pprint import pprint
from django.http import JsonResponse
from django.urls import reverse
from django.views import View
from account.models import User
from payment.models import Payment
from account.models import User



# Create your views here.

#def main():

# Check if payment is still in time

 # paymentList = Payment.objects.all()
  #for pay in paymentList:
 #   currentDay = localtime(now()).replace(hour=0, minute=0, second=0, microsecond=0)
    #if pay.last_day < currentDay:
     #   pay.active = False
      #  pay.save()
    #else:
     #   print("Granter")
    



# Check if user has acess
 # users = User.objects.all()
  #for user in users:
   # paymentByuser = Payment.objects.all().filter(user=user,active=True)
    #if not paymentByuser:
     #   user.is_student = False
      #  user.save()
    

#main()


@login_required()
def payment(request):
    
    return render(request, 'payment/payment.html')


@login_required()
def mpesa(request):
    return "Hello"

   

