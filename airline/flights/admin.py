from django.contrib import admin

# Register your models here.
from .models import Flight, Airport, Passenger

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger)