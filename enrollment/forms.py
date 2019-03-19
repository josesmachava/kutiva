from django import forms
from django.forms import ModelForm
from .models import Student


class StudentForm(ModelForm):
    class Meta:


        model = Student
        fields = '__all__'
        labels = {
            'name': '',
            'surname' : '',
            'phone_number':'',
            'email':''
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Apelido'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Numero de telefone'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'})
        }