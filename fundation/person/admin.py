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

    
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "get_name",
        "get_dni",
        "get_care_centers",
        "health_insurance"
    )
    fields = [
        "person"
        "medication",
        "health_insurance",
        "care_taker"
    ]

    def get_name(self, obj):
        return obj.person.name

    def get_dni(self, obj):
        return obj.person.dni

    def get_care_centers(self, obj):
        return "".join(obj.care_centers.all())

    get_name.short_description = "Name"
    get_dni.short_description = "DNI"
    get_care_centers.short_description = "Care Centers"


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = (
        "get_name",
        "get_dni",
    )
    fields = [
        "person",
    ]

    def get_name(self, obj):
        return obj.person.name

    def get_dni(self, obj):
        return obj.person.dni

    def get_care_centers(self, obj):
        return "".join(obj.care_centers.all())

    get_name.short_description = "Name"
    get_dni.short_description = "DNI"
    get_care_centers.short_description = "Care Centers"


@admin.register(HealthInsurance)
class HealthInsuranceAdmin(admin.ModelAdmin):
    list_display = ["name"]
    fields = ["name"]
