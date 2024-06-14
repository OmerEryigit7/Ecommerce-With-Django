from django.shortcuts import render,get_object_or_404
from .models import BlogModel

def blogs(request):
    blogs = BlogModel.objects.all()
    context = {
        "blogs":blogs
    }
    return render(request,"blogs.html",context)

def blog(request,slug):
    blog = get_object_or_404(BlogModel,slug=slug)
    context = {
        "blog":blog
    }
    return render(request,"blog.html",context)
