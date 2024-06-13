from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=1000,null=False,blank=False)

    def __str__(self):
        return f"{self.name}"
    

class ProductModel(models.Model):
    name = models.CharField(max_length=1000,null=False,blank=False)
    image = models.ImageField(upload_to="C:/Users/kayra/ecommerce/static/img")
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=False,blank=False)
    stock = models.IntegerField(null=False,blank=False)
    description = models.TextField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

class ReportModel(models.Model):
    firstname = models.CharField(max_length=100,null=False,blank=False)
    lastname = models.CharField(max_length=100,null=False,blank=False)
    email = models.CharField(max_length=100,null=False,blank=False)
    report = models.TextField()

    def __str__(self):
        return f"{self.report}"