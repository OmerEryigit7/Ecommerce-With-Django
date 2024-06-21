from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm,LoginUserForm,UpdateUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
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
            username = form.cleaned_data.get("username")

            hashed_password = make_password(password1)
            newUser = User.objects.create(password=hashed_password, first_name=first_name, last_name=last_name, email=email,username=username)
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

def loginuser(request):
    form = LoginUserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password1")

            user = authenticate(username=username,password=password1)
            if user is not None:
                messages.success(request,"Başarıyla Giriş Yapıldı")
                login(request,user)
                return redirect('index')
            else:
                messages.warning(request,"Böyle Bir Kullanıcı Bulunmuyor!")
        else:
            messages.warning(request,"Formu Doldururken Bir Hata Oluştu!")
    else:
        form = LoginUserForm()
    return render(request,"loginuser.html",{"form":form})

def LogoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Oturum Kapatıldı.")
    return redirect('index')

