from django.db import models

# Create your models here.
class items(models.Model):
    name=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    orign=models.CharField(max_length=200)
class cart(models.Model):
    username=models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    uid=models.BigIntegerField()
class cart2(models.Model):
    item=models.CharField(max_length=200)