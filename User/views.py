from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages

def createuser(request):
    form = UserForm(request.POST)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password1 = form.cleaned_data.get("password1")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")

        hashed_password = make_password(password1)
        newUser = User.objects.create(username=username,password=password1,first_name=first_name,last_name=last_name)
        newUser.save()

        login(request,newUser)

        messages.success(request,'Başarıyla Kayıt Olundu Ve Giriş Yapıldı')
        return redirect('index')
    else:
        messages.warning(request,"Formu Doldururken Bir Hata Yaptınız, Lütfen Tekrar Deneyin.")
    return render(request,"createuser.html",context)
