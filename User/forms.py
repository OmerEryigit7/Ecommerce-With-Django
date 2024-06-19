from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    username = forms.CharField(label="username", min_length=0, max_length=50, required=True)
    password1 = forms.CharField(label="Password",max_length=20,required=True)
    password2 = forms.CharField(label="Confirm Password",max_length=20,required=True)
    first_name = forms.CharField(max_length=20,min_length=3,required=False)
    last_name = forms.CharField(max_length=10,min_length=3,required=False)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2']