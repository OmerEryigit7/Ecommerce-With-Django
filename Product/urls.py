from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('Products/',views.products,name="products"),
    path('Product/<slug:slug>',views.product,name="product")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)