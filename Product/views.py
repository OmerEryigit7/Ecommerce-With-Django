from django.shortcuts import render,redirect,get_object_or_404
from .forms import ReportForm
from .models import ReportModel,ProductModel
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

def products(request):
    Products = ProductModel.objects.all()
    context = {
        "Products":Products
    }
    return render(request,"products.html",context)

def product(request,slug):
    Product = get_object_or_404(ProductModel,slug=slug)
    context = {
        "Product":Product
    }
    return render(request,"product.html",context)