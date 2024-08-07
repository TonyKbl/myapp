from django.contrib import admin
from .models import Page, PageFollow

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("page_name",)}

admin.site.register(Page, PageAdmin)
admin.site.register(PageFollow)