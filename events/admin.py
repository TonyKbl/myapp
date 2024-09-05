from django.contrib import admin
from .models import Event

# Register your models here.
class EventsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventsAdmin)