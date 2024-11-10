from django.contrib import admin
from .models import (
    MasterEvent,
    ClubEvent,
    Social,
    Meet,
    Event,
    Guestlist,
    # EventReview,
    EventHost,
)


# Register your models here.
class MasterEventAdmin(admin.ModelAdmin):
    list_display = ("title",)


class ClubEventAdmin(admin.ModelAdmin):
    list_display = ("title",)


class EventHostAdmin(admin.ModelAdmin):
    list_display = (
        "event",
        "host",
    )


class EventAdmin(admin.ModelAdmin):
    list_display = ("event", "date")


class GuestlistAdmin(admin.ModelAdmin):
    list_display = ("guest", "non_member", "event", "profile_type", "private")


admin.site.register(MasterEvent, MasterEventAdmin)
admin.site.register(ClubEvent, ClubEventAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventHost, EventHostAdmin)
# admin.site.register(EventReview)
admin.site.register(Social)
admin.site.register(Meet)
admin.site.register(Guestlist, GuestlistAdmin)
