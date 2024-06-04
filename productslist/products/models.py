from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(0)])
    number_of_items = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=timezone.now())
