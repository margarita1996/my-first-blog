from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Products(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)

    def __str__(self):
        return self.name


class Shops(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Manufactures(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)

    def __str__(self):
        return self.name



class ShopsAndProducts(models.Model):
    count = models.BigIntegerField()
    shop = models.ForeignKey(Shops)
    product = models.ForeignKey(Products)

    def __str__(self):
        return str(self.id)

class ProductsAndManufactures(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    product = models.ForeignKey(Products)
    manufacture = models.ForeignKey(Manufactures)

    def __str__(self):
        return str(self.id)


