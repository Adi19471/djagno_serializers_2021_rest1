from django.db import models

# Create your models here.
class LaptopDetailes(models.Model):
    name = models.CharField(max_length=120)
    company_name = models.CharField(max_length=160)
    date_type = models.DateField(auto_now_add=True)
    laptope_serial = models.CharField(max_length=250)

class NewLaptope(models.Model):
    latest_type = models.CharField(max_length=140)
    image = models.ImageField(upload_to='images')
    laptope_price = models.OneToOneField(LaptopDetailes,on_delete=models.CASCADE)
    city = models.CharField(max_length=150)
    product_description = models.TextField()