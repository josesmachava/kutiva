from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse
from cms.models import *


def index(request):
    courses = Course.objects.all()
    partners = Partner.objects.all()
    categories = Category.objects.all()

    testimonials = Testimonial.objects.all()
    if request.user.is_authenticated:
        return redirect('course')
    else:
        return render(request, 'kutiva/index.html', {'courses': courses, 'categories': categories, 'partners': partners,
                                                     'testimonials': testimonials})


def price(request):
    return render(request, 'kutiva/price.html')


def security(request):
    return render(request, "about/security.html")


def terms(request):
    return render(request, "about/terms.html")


def policies(request):
    return render(request, "about/policies.html")


def handler404(request, exception):
    return render(request, 'error/404.jade', status=404)



def handler500(request):
    return render(request, 'error/500.jade', status=500)
