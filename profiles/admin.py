from django.contrib import admin
from .models import Profile, Follow, LookingFor, BlockedList, Interest

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Follow)
admin.site.register(Interest)
# admin.site.register(UserLevel)
admin.site.register(LookingFor)
admin.site.register(BlockedList)



