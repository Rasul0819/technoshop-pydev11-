from django.db import models
from django.contrib.auth.models import AbstractUser
import random
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    phone_num = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    adres = models.CharField(max_length=300)
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, blank=True, null=True)

    def generate_verification_code(self):
        self.verification_code = str(random.randint(100000, 999999))
        self.save()

class Brand(models.Model):
    brand_name = models.CharField(max_length=250)
    slug = models.SlugField()

    def __str__(self):
        return self.brand_name


class Category(models.Model):
    category_name = models.CharField(max_length=250)
    slug = models.SlugField()

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=250)

    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    main_image = models.ImageField(upload_to='media/shop/')
    image2 = models.ImageField(upload_to='media/shop/',
                               blank=True,null=True)
    image3 = models.ImageField(upload_to='media/shop/',
                               blank=True,null=True)
    image4 = models.ImageField(upload_to='media/shop/',
                               blank=True,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.product_name

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return self.email
    




class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.product_name} ({self.quantity})"
