from django.db import models
from drugbank.models import Drug
from institution.models import Institution
from django.db.models import CheckConstraint, Q, F


class Person(models.Model):
    name = models.CharField(max_length=40)
    dni = models.IntegerField()
    address = models.CharField(max_length=40)
    phone_number = models.IntegerField()
    email = models.EmailField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "dni"],
                name='name_and_dni_person_restiction'
            )
        ]


class HealthInsurance(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class HealthProfessional(models.Model):
    person = models.OneToOneField(Person, on_delete=models.PROTECT)

    def __str__(self):
        return self.preson.name


class Patient(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    medication = models.ForeignKey(
        Drug,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    care_centers = models.ManyToManyField(Institution, blank=True)
    health_insurance = models.OneToOneField(
        HealthInsurance,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    care_taker = models.ForeignKey(
        Person,
        on_delete=models.PROTECT,
        related_name="persons"
    )

    def __str__(self):
        return self.person.name

    class Meta:
        constraints = [
            CheckConstraint(
                check=~Q(care_taker=F('person')),
                name='check_person_is_not_care_taker',
            ),
        ]


class Volunteer(models.Model):
    person = models.OneToOneField(Person, on_delete=models.PROTECT)

    def __str__(self):
        return self.person.name


class VolunteerInInstitution(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.volunteer.name} in {self.institution.name}"
