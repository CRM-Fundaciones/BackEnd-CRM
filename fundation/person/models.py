from django.db import models
from drugbank.models import Drug
from institution.models import Institution


class Person(models.Model):
    name = models.CharField(max_length=40)
    dni = models.IntegerField()
    address = models.CharField(max_length=40)
    phone_number = models.IntegerField()
    email = models.EmailField()
    created_at = models.DateField()


class HealthInsurance(models.Model):
    name = models.CharField(max_length=40)


class HealthProfessional(models.Model):
    person = models.OneToOneField(Person, on_delete=models.PROTECT)


class Patient(models.Model):
    person = models.OneToOneField(Person, on_delete=models.PROTECT)
    medication = models.ForeignKey(Drug, on_delete=models.PROTECT)
    care_center = models.ManyToManyField(Institution)
    health_insurance = models.OneToOneField(HealthInsurance, on_delete=models.PROTECT)
    care_taker = models.ForeignKey(Person, on_delete=models.PROTECT, related_name="persons")
    

class Volunteer(models.Model):
    person = models.OneToOneField(Person, on_delete=models.PROTECT)
    

class VolunteerInInstitution(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()