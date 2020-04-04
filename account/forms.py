from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student
from django.db import transaction
from django.forms import ModelForm
from cms.models import  Institution
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder': 'Search'}) )
    last_name = forms.CharField(max_length=30, required=False,)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )




class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='Nome',  required=True, widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    last_name = forms.CharField(max_length=30, label='Apelido', required=True    , widget=forms.TextInput(attrs={'placeholder': 'Apelido'}))
    email = forms.EmailField(max_length=254, label='Email',  widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    password1 = forms.CharField(label='Palavra passe',  widget=forms.PasswordInput(attrs={'placeholder': 'Palavra Passe'}))
    password2 = forms.CharField(label='Repitir Palavra Passe ',  widget=forms.PasswordInput(attrs={'placeholder': 'Repitir Palavra Passe  '}))
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
    photo = forms.FileField()
    first_name = forms.CharField(label="Nome", widget=forms.TextInput(attrs={'placeholder': 'Nome'}), max_length=30, required=False)
    last_name = forms.CharField(label="Apelido", widget=forms.TextInput(attrs={'placeholder': 'Apelido'}), max_length=30, required=False)
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'E-mail'}), max_length=254, required=False)
    location = forms.CharField(label="Província", widget=forms.TextInput(attrs={'placeholder': 'Província'}), max_length=30, required=False)
    phone_number = forms.CharField(label="Número de telefone", widget=forms.TextInput(attrs={'placeholder': 'Número de telefone'}), max_length=30)
    description = forms.CharField(label="Biografia",widget=forms.Textarea(attrs={'placeholder': 'Sobre me'}), max_length=30, required=False)
    educational_institution = forms.CharField(label="Instituição de ensino", widget=forms.TextInput(attrs={'placeholder': 'Instuticao de ensino'}), max_length=30, required=False)
    role = forms.CharField(label="Profisacao", widget=forms.TextInput(attrs={'placeholder': 'Estudante'}),
                                  max_length=30, required=False)

    birth_date = forms.DateField(widget=forms.SelectDateWidget)
        
    
    class Meta:
        model = Student
        fields = ('photo', 'first_name', 'last_name', 'email', 'role', 'location', 'birth_date', 'educational_institution', 'phone_number', 'description')


      