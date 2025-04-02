from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    
    def __str__(self):
        return self.name
    

    