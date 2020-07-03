from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.TextField(null=False)
    price = models.FloatField(null=False)
    amount = models.IntegerField(null=False)

    def create(self):
        self.save()

    def __str__(self):
        return self.name