from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:        
        model = Profile
        fields = ("headline", "intro")
        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control'}),
            'intro': forms.TextInput(attrs={'class': 'form-control'}),
        }

        def __str__(self):
            return self.User