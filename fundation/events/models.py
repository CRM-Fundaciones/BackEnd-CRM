from django.db import models
from places.models import Address

EVENT_MODALITY = [
    ("VIRTUAL", "Virtual"),
    ("PRESENCIAL", "Presencial")
]

EVENT_THEMES = [
    ("SALUD", "Salud"),
    ("HABITOS", "Hábitos"),
    ("EXTRAS", "Extras"),
    ("UNION", "Unión")
]

EVENT_TYPES = [
    ("CHARLA", "Charla"),
    ("EVENTO", "Evento"),
    ("CONFERENCIA", "Conferencia"),
    ("CICLO", "Ciclo")
]

DAYS = [
    ("LUNES", "Lunes"),
    ("MARTES", "Martes"),
    ("MIERCOLES", "Miércoles"),
    ("JUEVES", "Jueves"),
    ("VIERNES", "Viernes"),
    ("SABADO", "Sabado"),
    ("DOMINGO", "Domingo"),
]

EVENT_ROLES = [
    ("ORGANIZADOR", "Organizador"),
    ("PARTICIPANTE", "Participante"),
    ("DONANTE", "Donante")
]
    

class Event(models.Model):
    date = models.DateTimeField()
    name = models.CharField(default="", max_length=50)
    place = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    modality = models.CharField(choices=EVENT_MODALITY, max_length=20, default="")
    theme = models.CharField(choices=EVENT_THEMES, max_length=20, default="")
    event_type = models.CharField(choices=EVENT_TYPES, max_length=20, default="")

