from django.contrib import admin
from .models import Post, PagePost, Like, PageLike

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(PagePost, PostAdmin)
admin.site.register(Like, PostAdmin)
admin.site.register(PageLike, PostAdmin)