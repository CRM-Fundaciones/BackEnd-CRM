from django.contrib import admin
from person.models import HealthInsurance, Person, Patient, Volunteer

admin.autodiscover()
admin.site.enable_nav_sidebar = False


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "dni", "address", "email")
    search_fields = [
        "name",
        "dni"
    ]
    fields = [
        "name",
        "dni",
        "email",
        "address",
        "phone_number"
    ]

# Register your models here.
