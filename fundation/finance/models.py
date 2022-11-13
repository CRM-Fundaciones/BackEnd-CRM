from django.db import models
from person.models import Person
from drugbank.models import Drug


class Purchase(models.Model):
    reason = models.CharField(max_length=500)
    date = models.DateTimeField()
    buyer = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=1)
    

class Sale(models.Model):
    date = models.DateTimeField()
    seller = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Product(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.SET_NULL, null=True)
    drug = models.ForeignKey(Drug, on_delete=models.SET_NULL, null=True)
    sale = models.ForeignKey(Sale, on_delete=models.SET_NULL, null=True)
