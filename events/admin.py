from django.contrib import admin
from .models import Event, EventDate, EventReview

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location')

class EventDateAdmin(admin.ModelAdmin):
    list_display = ('event', 'date')
    

admin.site.register(Event, EventAdmin)
admin.site.register(EventDate, EventDateAdmin)
admin.site.register(EventReview)