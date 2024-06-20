from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    password1 = forms.CharField(label="Password",max_length=20,required=True)
    first_name = forms.CharField(max_length=20,min_length=3,required=False)
    last_name = forms.CharField(max_length=10,min_length=3,required=False)
    email = forms.EmailField(max_length=256,min_length=0,required=True)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','password1','email']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data