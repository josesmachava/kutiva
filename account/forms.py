from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student
from django.db import transaction
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder': 'Search'}) )
    last_name = forms.CharField(max_length=30, required=False,)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )




class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='',  required=True, widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    last_name = forms.CharField(max_length=30, label='', required=True  , widget=forms.TextInput(attrs={'placeholder': 'Apelido'}))
    email = forms.EmailField(max_length=254, label='',  widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    password1 = forms.CharField(label='',  widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    password2 = forms.CharField(label='',  widget=forms.PasswordInput(attrs={'placeholder': 'Repitir Senha'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1')
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_instructor = False
        user.is_student = False
       
        user.save()

        student = Student.objects.create(user=user)
        return user        





class StudentSignUpdateForm(ModelForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    location = forms.CharField(max_length=30, required=False, help_text='Optional.')
    birth_date = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget)
        
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'location', 'birth_date')


      