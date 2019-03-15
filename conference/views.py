from django.shortcuts import render


# Create your views here.

def speaker(request):
    return render(request, 'conference/speaker.html')
