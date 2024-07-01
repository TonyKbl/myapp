from django import forms
from .models import Page
from django.contrib.auth.models import User


class PageCreateForm(forms.ModelForm):
        
    class Meta:        
        model = Page
        fields = (
            "page_type",
            "page",
            "address1",
            "address2",
            "town_city",
            "county",
            "post_code",
            "description",
        )

        def __str__(self):
            return self.model.page

class PageUpdateForm(forms.ModelForm):
        
    class Meta:        
        model = Page
        fields = (
            "page_type",
            "page",
            "address1",
            "address2",
            "town_city",
            "county",
            "post_code",
            "description",
        )