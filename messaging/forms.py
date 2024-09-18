from django import forms
from .models import Message
from django.contrib.auth.models import User

class MessageSendForm(forms.ModelForm):
    
    class Meta:        
        model = Message
        fields = (
            "message",
            )
        widgets = {
            'message': forms.Textarea(attrs={'rows': '3'}),
        }

        def __str__(self):
            return self.user