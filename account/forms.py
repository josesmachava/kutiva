from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student
from django.db import transaction


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )




class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
  
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email')
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_instructor = False
        user.is_student = False
       
        user.save()

        student = Student.objects.create(user=user)
        return user        