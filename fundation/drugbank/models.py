from django.db import models
from django.utils import timezone
from events.models import Event


class DrugBatch(models.Model):
    stock = models.IntegerField()
    prescription = models.FileField()
    

class Drug(models.Model):
    generic_name = models.CharField(max_length=100, default="")
    dosage = models.CharField(max_length=100, default="")
    drug_type = models.CharField(max_length=50, default="")
    expiration_date = models.DateTimeField(default=timezone.now())
    batch = models.ForeignKey(DrugBatch, on_delete=models.SET_NULL, null=True)

    def get_medication_type(self):
        return self.drug_type

    def get_expiration_date(self):
        return self.expiration_date

    def get_prescription(self):
        return self.batch.prescription


class DrugBank(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    drugs = models.ManyToManyField(Drug)

    def get_stock(self):
        return self.drugs.values("generic_name").annotate(stock=models.Count("generic_name")).order_by()

    def get_event_date(self):
        return self.event.date

    
