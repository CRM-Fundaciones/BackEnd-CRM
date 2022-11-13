from django.db import models
from drugbank.models import Drug
from places.models import Address
from institution.models import Institution
from django.db.models import CheckConstraint, Q, F
from events.models import EVENT_ROLES, Event, DAYS


class Person(models.Model):
    name = models.CharField(max_length=40, default="")
    dni = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
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
    name = models.CharField(max_length=40, default="")

    def __str__(self):
        return self.name


class HealthProfessional(models.Model):
    person = models.OneToOneField(Person, on_delete=models.PROTECT)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    work_modality = models.CharField(max_length=50, default="")
    

    def __str__(self):
        return self.person.name


class Patient(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    medication = models.ForeignKey(
        Drug,
        blank=True,
        null=True,
        on_delete=models.SET_NULL, 
    )
    care_centers = models.ManyToManyField(Institution, blank=True)
    health_insurance = models.OneToOneField(
        HealthInsurance,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
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


class Session(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    professional = models.ForeignKey(HealthProfessional, on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ticket = models.FileField()
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    modality = models.CharField(max_length=50, default="")


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


class Comment(models.Model):
    text = models.CharField(max_length=500, default="")
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    
class PersonInEvent(models.Model):
    persons = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    events = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    role = models.CharField(choices=EVENT_ROLES,max_length=50, default="")


class Course(models.Model):
    theme = models.CharField(max_length=50, default="")
    professor = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)


class Schedule(models.Model):
    courses = models.ManyToManyField(Course)
    day = models.CharField(choices=DAYS, max_length=10, default="")
    start_time = models.TimeField()
    duration = models.IntegerField()