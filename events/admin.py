from django.contrib import admin
from .models import Events

# Register your models here.
class EventsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Events, EventsAdmin)