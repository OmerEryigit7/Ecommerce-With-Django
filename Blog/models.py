from django.db import models
from django.utils.text import slugify

class BlogModel(models.Model):
    name = models.CharField(max_length=1000,null=False,blank=False)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="C:/Users/kayra/ecommerce/static/img")
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True)

    def __str__(self):
        return f"{self.name}"
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)
