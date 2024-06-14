from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Blogs/',views.blogs,name="blogs"),
    path('Blog/<slug:slug>',views.blog,name="blog")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)