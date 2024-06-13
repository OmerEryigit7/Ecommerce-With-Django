from django.contrib import admin
from .models import ReportModel,ProductModel,Category

admin.site.register(ReportModel)
admin.site.register(ProductModel)
admin.site.register(Category)
