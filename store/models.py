from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True) #max_length etc.. are attributes
    slug = models.SlugField(max_length=255, unique=True) #slug enables categorizing when searching, should only have one hance category name should be unique

    #data over data, more instructions to provide for django for our moels
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):#our second table
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE) #this is a foregin key 
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #calling the products, we can sort it with meta class
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',) #the negative returns the products in the order the were last created
    
    def __str__(self):
        return self.title