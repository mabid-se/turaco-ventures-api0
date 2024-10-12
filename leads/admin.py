from django.contrib import admin

# Register your models here.
from .models import Leads


@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "contact_number",
        "name",
        "persons",
        "follow_up",
        "status",
        "destination",
        "dates",
        "city",
        "details",
    )
