from django.contrib import admin
from .models import Post, PagePost

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(PagePost, PostAdmin)