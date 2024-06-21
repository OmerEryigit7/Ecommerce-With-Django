from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserForm(UserCreationForm):
    username = forms.CharField(label="Kullanıcı Adı",max_length=20,required=True)
    password1 = forms.CharField(label="Parola",max_length=20,required=True)
    password2 = forms.CharField(label="Parolayı Doğrula",max_length=20,required=True)
    first_name = forms.CharField(max_length=20,min_length=3,required=False)
    last_name = forms.CharField(max_length=10,min_length=3,required=False)
    email = forms.EmailField(max_length=256,min_length=0,required=True)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','password1','password2','email','username']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            return ValidationError("Şifreler Eşleşmiyor!")
        return cleaned_data
    
class LoginUserForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı",max_length=20,required=True)
    password1 = forms.CharField(label="Parola",max_length=20,required=True)
    password2 = forms.CharField(label="Parolayı Doğrula",max_length=20,required=True)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            return ValidationError("Şifreler Eşleşmiyor!")
        return cleaned_data
    


