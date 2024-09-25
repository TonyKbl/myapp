from django.contrib import admin
from .models import Blog, Tag, Catagory

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user = request.user
        return qs if user.is_superuser else qs.filter(author=user.id)
    

    list_display = ('title', 'author', 'catagory')    
    exclude = ('author', 'slug' )
    
    def save_model(self, request, obj, form, change,):
        
        if getattr(obj, 'author', None) is None:
            obj.author = request.user

        obj.save()
    

class CatagoryAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, CatagoryAdmin)
admin.site.register(Catagory, TagAdmin)