from django.contrib.gis import admin
from .models import Report, ReportedMessage, ReportedPage, ReportedPhoto, ReportedProfile

# Register your models here.
class ReportAdmin(admin.ModelAdmin):
    pass

    
admin.site.register(Report, ReportAdmin)
# admin.site.register(Page, PageAdmin)
admin.site.register(ReportedMessage)
admin.site.register(ReportedPage)
admin.site.register(ReportedPhoto)
admin.site.register(ReportedProfile)