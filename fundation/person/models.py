from django.db import models
from drugbank.models import Drug
from institution.models import Institution
from django.core.validators import MinValueValidator, MaxValueValidator


class Person(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    dni = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=False, blank=False)
    address = models.CharField(max_length=40, null=True)
    phone_number = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(11)], null=True)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, db_index=True, null=False, blank=False)


class HealthInsurance(models.Model):
    name = models.CharField(max_length=40)


class HealthProfessional(models.Model):
    person = models.OneToOneField(Person, on_delete=models.SET_NULL, null=True)


class Patient(models.Model):
    person = models.OneToOneField(Person, on_delete=models.SET_NULL, null=True)
    medication = models.ForeignKey(Drug, on_delete=models.SET_NULL, null=True)
    care_centers = models.ManyToManyField(Institution)
    health_insurance = models.OneToOneField(HealthInsurance, on_delete=models.SET_NULL, null=True)
    care_taker = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name="persons")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["person", "care_taker"], name="all_keys_unique_together")
        ]
    

class Volunteer(models.Model):
    person = models.OneToOneField(Person, on_delete=models.SET_NULL, null=True)
    

class VolunteerInInstitution(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.SET_NULL, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()