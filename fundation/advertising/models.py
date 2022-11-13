from django.db import models
from person.models import Comment

class AdvertisingBatch(models.Model):
    print_date = models.DateTimeField()
    print_amount = models.IntegerField()
    delivered_amount = models.IntegerField()
    width = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    ad_type = models.CharField(max_length=50, default="")
    objective = models.CharField(max_length=500, default="")
    comments = models.ManyToManyField(Comment)
    image = models.ImageField()