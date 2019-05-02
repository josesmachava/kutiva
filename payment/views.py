import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime  
from datetime import timedelta
# Create your views here.

from django.contrib.auth.decorators import login_required

from pprint import pprint
from django.http import JsonResponse
from django.urls import reverse
from django.views import View
from account.models import User
from payment.models import payment
from payment.api import APIContext, APIMethodType, APIRequest
from account.models import User


# Create your views here.

def main():

# Check if payment is still in time

  payments = payment.objects.all()
  nowdate = datetime.now()

  for paid in payments:
    day = paid.last_day
    if day > nowdate:
        print("maior")
    else:
        print("menor")


# Check if user has acess
  users = User.objects.all()
  for user in users:
    paymentByuser = payment.objects.all().filter(user=user,active=True)
    if not paymentByuser:
        user.is_student=False
        # print(user,"FAlse")
    

main()


@login_required()
def Payment(request):

    return render(request, 'payment/payment.html')


@login_required()
def Mpesa(request):
    contact = str(258) + str(request.POST['contact'])
    amount = '750'
    reference = 'kutiva'
    api_context = APIContext()
    api_context.api_key = '9njrbcqty9ew3cyx4s6k7jvtab134rr6'
    api_context.public_key = 'MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAmptSWqV7cGUUJJhUBxsMLonux24u+FoTlrb+4Kgc6092JIszmI1QUoMohaDDXSVueXx6IXwYGsjjWY32HGXj1iQhkALXfObJ4DqXn5h6E8y5/xQYNAyd5bpN5Z8r892B6toGzZQVB7qtebH4apDjmvTi5FGZVjVYxalyyQkj4uQbbRQjgCkubSi45Xl4CGtLqZztsKssWz3mcKncgTnq3DHGYYEYiKq0xIj100LGbnvNz20Sgqmw/cH+Bua4GJsWYLEqf/h/yiMgiBbxFxsnwZl0im5vXDlwKPw+QnO2fscDhxZFAwV06bgG0oEoWm9FnjMsfvwm0rUNYFlZ+TOtCEhmhtFp+Tsx9jPCuOd5h2emGdSKD8A6jtwhNa7oQ8RtLEEqwAn44orENa1ibOkxMiiiFpmmJkwgZPOG/zMCjXIrrhDWTDUOZaPx/lEQoInJoE2i43VN/HTGCCw8dKQAwg0jsEXau5ixD0GUothqvuX3B9taoeoFAIvUPEq35YulprMM7ThdKodSHvhnwKG82dCsodRwY428kg2xM/UjiTENog4B6zzZfPhMxFlOSFX4MnrqkAS+8Jamhy1GgoHkEMrsT5+/ofjCx0HjKbT5NuA2V/lmzgJLl3jIERadLzuTYnKGWxVJcGLkWXlEPYLbiaKzbJb2sYxt+Kt5OxQqC1MCAwEAAQ=='
    api_context.ssl = True
    api_context.method_type = APIMethodType.POST
    api_context.address = 'api.sandbox.vm.co.mz'

    api_context.port = 18346
    api_context.path = '/ipg/v1/c2bpayment/'

    api_context.add_header('Origin', '*')

    api_context.add_parameter('input_ThirdPartyReference', '8e090ace-e41b-4606-b320-0286a0b388da')
    api_context.add_parameter('input_Amount', amount)
    api_context.add_parameter('input_CustomerMSISDN', contact)
    api_context.add_parameter('input_ServiceProviderCode', '171717')
    api_context.add_parameter('input_TransactionReference', reference)

    api_request = APIRequest(api_context)
    result = json.dumps(api_request.execute())
    data = json.loads(result)
    print(request.user)
    if data['status_code'] == 422:
        
        data_end = datetime.now() + timedelta(days=30)
        ops = payment(number_sender=contact, mount=1000,last_day=data_end,user=request.user)
        ops.save()
        user = User.objects.get(pk = request.user.id)
        user.is_student =True
        user.save()
        print (user)
        return HttpResponseRedirect(reverse(viewname="index"))

    if data['status_code'] == 409:
        print("Duplicaçao de transiçao")
        return HttpResponseRedirect(reverse(viewname="index"))
    else:
        print("something went wrong")
        return HttpResponseRedirect(reverse(viewname="index"))
   

