from django import forms
from .models import Event, EventDate
from pages.models import Page, PageHost
from django.contrib.auth.models import User


class EventCreateForm(forms.ModelForm):

    # host_list = forms.ModelMultipleChoiceField(
    #     # choices = 'host_choices',
    #     queryset=PageHost.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True)

   
    class Meta:        
        model = Event
        fields = (
            "title",
            "description",
            "image",
            "host_list"
        )
        
    def get_context_data(self, *args, **kwargs):
        context = super(EventCreateForm, self).get_context_data(*args, **kwargs)
        context['host_choices'] = PageHost.objects.filter(page_name_id=self.kwargs['pk'])
        return context
        
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