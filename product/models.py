from django.db import models

# Create your models here.

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Product(models.Model):
    name=models.CharField(max_length=80)
    categories=models.CharField(max_length=200)
    color=models.CharField(max_length=50)
    size=models.CharField(max_length=80)
    stock=models.CharField(max_length=200)
    price=models.IntegerField()
    brand=models.CharField(max_length=200)
    weight= models.IntegerField()
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    
