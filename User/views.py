from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.contrib import messages

def createuser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get("password1")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")

            hashed_password = make_password(password1)
            newUser = User.objects.create(password=hashed_password, first_name=first_name, last_name=last_name, email=email)
            newUser.save()

            login(request, newUser)

            messages.success(request, 'Başarıyla Kayıt Olundu Ve Giriş Yapıldı')
            return redirect('index')
        else:
            messages.warning(request, form.errors)
            print(form.errors)
    else:
        form = UserForm()
    return render(request, "createuser.html", {"form": form})