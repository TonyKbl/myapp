from django import forms
from .models import Events
from pages.models import Page
from django.contrib.auth.models import User


class EventCreateForm(forms.ModelForm):
        
    class Meta:        
        model = Events
        fields = (
            "title",
            "description",
            "image",
        )
        # location = forms.ModelChoiceField(queryset=Page.objects.all())
        def __str__(self):
            return self.model.page