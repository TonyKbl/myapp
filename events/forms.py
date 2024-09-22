from django import forms
from .models import Event, EventDate
from pages.models import Page, PageHost
from django.contrib.auth.models import User


class EventCreateForm(forms.ModelForm):

    host_list = forms.ModelMultipleChoiceField(
        queryset=PageHost.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True)

   
    class Meta:        
        model = Event
        fields = (
            "title",
            "description",
            "image",
        )
        
        
class EventAddDatesForm(forms.ModelForm):

    class Meta:        
        model = EventDate
        fields = (
            "date",
            "start_time",
            "end_time",
            "admission_fees",
            "additional_info",
        )

        widgets={
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }