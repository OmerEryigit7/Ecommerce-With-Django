from django.contrib import admin
from django.urls import path
from Product import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('Product/',include('Product.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
