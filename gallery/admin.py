from django.contrib import admin
from .models import UserGallery

# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserGallery, GalleryAdmin)