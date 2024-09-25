from django.contrib import admin
from .models import Blog, Tags

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tags, BlogAdmin)