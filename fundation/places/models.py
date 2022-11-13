from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50, default="")


class City(models.Model):
    name = models.CharField(max_length=50, default="")
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)


class Address(models.Model):
    name = models.CharField(max_length=70, default="")
    number = models.IntegerField()
    floor = models.IntegerField(null=True, blank=True)
    apartment = models.CharField(null=True, blank=True, max_length=3, default="")
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

