from django.core import validators
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


#from .models import UserSignUpModel,LoginModel

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        
class ProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labrls = {'email':'Email'}

class ContactForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField(max_length=50)
    message = forms.CharField(widget=forms.Textarea,max_length=2000)
