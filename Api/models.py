from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField

# Create your models here.

class Menu(models.Model):
    item_name = models.CharField(max_length=200)
    price = models.IntegerField(null=False)


    def __str__(self):
        return self.item_name




class Cart(models.Model):
    user = OneToOneField(User,default='anomonus',blank=True,on_delete=models.CASCADE)
    menus = models.ManyToManyField(Menu)

    
