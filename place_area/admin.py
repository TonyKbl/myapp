from django.contrib import admin
from .models import Region, PostCode, OuterPostCode

# Register your models here.
class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("region_name",)}

admin.site.register(Region, RegionAdmin)

admin.site.register(PostCode)

admin.site.register(OuterPostCode)