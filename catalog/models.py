from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class Producer(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    description = models.TextField(max_length=512)
    photo = models.FileField(upload_to='goods_photo/')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)