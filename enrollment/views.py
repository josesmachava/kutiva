from django.shortcuts import render
from .forms import StudentForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data['phone_number'])
            form.save(commit=True)
            return render(request, 'sucess.html')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = StudentForm()

    return render(request, 'index.html' , {'form': form})