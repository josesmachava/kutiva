from django.shortcuts import render

# Create your views here.


def security(request):
    return render(request, "about/security.html")

def terms(request):
    return render(request, "about/terms.html")

def policies(request):
    return render(request, "about/policies.html")

