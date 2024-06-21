from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('createuser/',views.createuser,name="createuser"),
    path('loginuser/',views.loginuser,name="loginuser"),
    path('logout/',views.LogoutUser,name="logout")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)