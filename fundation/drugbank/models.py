from django.db import models

class Drug(models.Model):
    pass
    '''
    generic_name = 
    dosage = 
    amount = 
    drug_type = 
    '''


class DrugBank(models.Model):
    pass
    '''
    event_date = models.RELACION?(Events)
    drugs = models.ManyToManyField(Drug, on_delete=models.CASCADE, related_name="drug_bank") 
    event_person = models.RELACION?(Person)?
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="drug_bank")
    '''


