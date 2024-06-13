from django.shortcuts import render,redirect
from .forms import ReportForm
from .models import ReportModel
from django.contrib import messages

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    form = ReportForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        form.save()
        messages.success(request,'Bildiriminiz Başarıyla İletildi,Teşekkür Ederiz.')
        return redirect('index')
    else:
        print(form.errors)
    return render(request,"contact.html",context)