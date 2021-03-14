from django.db import models


# Create your models here.
class orders(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    orderedproduct= models.CharField(max_length=100)
