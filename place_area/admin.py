from django.contrib import admin
from .models import Region

# Register your models here.
class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("region_name",)}

admin.site.register(Region, RegionAdmin)