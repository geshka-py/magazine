from django.db import models
from catalog.models import Product
from django.contrib.auth.models import User


class Status(models.Model):
    name = models.CharField(max_length=255)


class Order(models.Model):
    count = models.PositiveIntegerField()
    # status = models.ForeignKey(Status, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
