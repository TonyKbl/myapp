from django.contrib import admin
from .models import Profile, Follow, LookingFor, BlockedList

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Follow)
# admin.site.register(Level)
# admin.site.register(UserLevel)
admin.site.register(LookingFor)
admin.site.register(BlockedList)



