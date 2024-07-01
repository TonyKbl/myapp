from django import forms
from .models import Page
from django.contrib.auth.models import User

class PageCreateForm(forms.ModelForm):
        
    class Meta:        
        model = Page
        fields = (
            "page_type",
        )

class PageUpdateForm(forms.ModelForm):
        
    class Meta:        
        model = Page
        fields = (
            "page_type",
        )