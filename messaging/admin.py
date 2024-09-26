from django.contrib import admin
from .models import Message

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ('msg_from', 'msg_to','read', 'message', 'date_sent')

admin.site.register(Message, MessageAdmin)

