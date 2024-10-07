from django.contrib.gis import admin
from .models import Page, PageFollow, PageReviews, ClaimPage, PageHost

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("page_name",)}

class HostAdmin(admin.ModelAdmin):   
    list_display = ('page_name', 'host')
admin.site.register(Page, admin.GISModelAdmin)
# admin.site.register(Page, PageAdmin)
admin.site.register(PageFollow)
admin.site.register(PageHost, HostAdmin)
admin.site.register(PageReviews)
admin.site.register(ClaimPage)