from django.db import models

class Institution(models.Model):
    name = models.CharField(max_length=40)


class Contract(models.Model):
    start_time = models.DateField()
    end_time = models.DateField()
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)