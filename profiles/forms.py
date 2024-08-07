from django import forms
from .models import Profile
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:        
        model = Profile
        fields = (
            "profile_type",
            "display_name",
            "headline", 
            "intro", 
            "description", 
            "location", 
            "name",
            "DOB",
            "sexuality",
            "height",
            "body_type",
            "smoke",
            "drink",
            "name2",
            "DOB2",
            "sexuality2",
            "height2",
            "body_type2",
            "smoke2",
            "drink2",
            )
        widgets = {
            'profile_type': forms.Select(attrs={'class': 'form-control'}),
            'display_name': forms.TextInput(attrs={'class': 'form-control'}),
            'headline': forms.TextInput(attrs={'class': 'form-control'}),
            'intro': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'DOB': forms.DateInput(attrs={'class': 'form-control'}),
            'sexuality': forms.Select(attrs={'class': 'form-control'}),
            'height': forms.Select(attrs={'class': 'form-control'}),
            'body_type': forms.Select(attrs={'class': 'form-control'}),
            'smoke': forms.Select(attrs={'class': 'form-control'}),
            'drink': forms.Select(attrs={'class': 'form-control'}),
            'name2': forms.TextInput(attrs={'class': 'form-control'}),
            'DOB2': forms.DateInput(attrs={'class': 'form-control'}),
            'sexuality2': forms.Select(attrs={'class': 'form-control'}),
            'height2': forms.Select(attrs={'class': 'form-control'}),
            'body_type2': forms.Select(attrs={'class': 'form-control'}),
            'smoke2': forms.Select(attrs={'class': 'form-control'}),
            'drink2': forms.Select(attrs={'class': 'form-control'}),
        }

        def __str__(self):
            return self.user