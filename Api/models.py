from django.db import models

# Create your models here.

class Menu(models.Model):
    item_name = models.CharField(max_length=200)
    price = models.IntegerField(null=False)


    def __str__(self):
        return self.item_name

class Cart(models.Model):
    item_name = models.CharField(max_length=200)
    price = models.IntegerField(null=False)

    def __str__(self):
        return self.item_name
