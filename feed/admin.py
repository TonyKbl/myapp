from django.contrib import admin
from .models import Post, PagePost, PostLike, PagePostLike

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(PagePost, PostAdmin)
admin.site.register(PostLike, PostAdmin)
admin.site.register(PagePostLike, PostAdmin)