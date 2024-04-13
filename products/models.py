from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    SIZE_CHOICES = [
        ('OS', 'One Size'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]
   
    category = models.ManyToManyField('Category', blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    size = models.CharField(max_length=3, choices=SIZE_CHOICES, null=True, blank=True)
    color = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

