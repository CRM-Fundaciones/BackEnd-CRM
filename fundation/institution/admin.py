from django.contrib import admin

from institution.models import Contract, Institution

class ContractInline(admin.TabularInline):
    model = Contract
    fields = ["start_time", "end_time"]


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ["name"]
    fields = ["name"]
    inlines = [ContractInline]
    def get_contracts(self, obj):
        return 


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ["start_time", "end_time"]
    fields = ["institution", "start_time", "end_time"]
