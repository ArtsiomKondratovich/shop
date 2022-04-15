from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class City(models.Model):
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.city


class Shop(models.Model):
    name_of_shop = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    house = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('shop_detail', args={'pk': self.pk})

    def __str__(self):
        return self.name_of_shop

class PersonCabinet(models.Model):
    phone = models.CharField(max_length=12)
    street = models.CharField(max_length=120)
    home = models.CharField(max_length=3)
    date_of_birth = models.DateField()
    users = models.OneToOneField('User', on_delete=models.CASCADE)
