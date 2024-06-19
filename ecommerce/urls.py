from django.contrib import admin
from django.urls import path
from Product import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Product/',include('Product.urls')),
    path('Blog/',include('Blog.urls')),
    path('User/',include('User.urls')),
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
