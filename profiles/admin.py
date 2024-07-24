from django.contrib import admin
from .models import Profile, Follow

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Follow)



