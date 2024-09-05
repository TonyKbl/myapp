from django import forms
from .models import Event
from pages.models import Page
from django.contrib.auth.models import User


class EventCreateForm(forms.ModelForm):
        
    class Meta:        
        model = Event
        fields = (
            "title",
            "description",
            "image",
            "date",
            "start_time",
            "end_time",
        )

        widgets={
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

        location = forms.ModelChoiceField(queryset=Page.objects.all())
        def __str__(self):
            return self.model.page