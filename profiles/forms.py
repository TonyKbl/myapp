from django import forms
from .models import Profile
from django.contrib.auth.models import User


class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:        
        model = Profile
        fields = (
            "profile_type", 
            "headline", 
            "intro", 
            "description", 
            "location", 
            "name",
            "DOB",
            "sexuality",
            "height",
            "name2",
            "DOB2",
            "sexuality2",
            "height2",
            )
        widgets = {
            'profile_type': forms.Select(attrs={'class': 'form-control'}),
            'headline': forms.TextInput(attrs={'class': 'form-control'}),
            'intro': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'DOB': forms.DateInput(attrs={'class': 'form-control'}),
            'sexuality': forms.Select(attrs={'class': 'form-control'}),
            'height': forms.Select(attrs={'class': 'form-control'}),
            'bodytype': forms.Select(attrs={'class': 'form-control'}),
            'smoke': forms.Select(attrs={'class': 'form-control'}),
            'drink': forms.Select(attrs={'class': 'form-control'}),
            'name2': forms.TextInput(attrs={'class': 'form-control'}),
            'DOB2': forms.DateInput(attrs={'class': 'form-control'}),
            'sexuality2': forms.Select(attrs={'class': 'form-control'}),
            'height2': forms.Select(attrs={'class': 'form-control'}),
            'bodytype2': forms.Select(attrs={'class': 'form-control'}),
            'smoke2': forms.Select(attrs={'class': 'form-control'}),
            'vape2': forms.Select(attrs={'class': 'form-control'}),
        }

        def __str__(self):
            return self.user