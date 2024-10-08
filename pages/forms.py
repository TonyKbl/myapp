from django import forms
from .models import Page, PageReviews, ClaimPage, PageHost
from django.contrib.auth.models import User


class PageCreateForm(forms.ModelForm):
        
    class Meta:        
        model = Page
        fields = (
            "page_type",
            "page_name",
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
            "page_name",
            "address1",
            "address2",
            "town_city",
            "county",
            "post_code",
            "region",
            "description",
        )

class PageReviewForm(forms.ModelForm):
    
    class Meta:
        model = PageReviews
        fields = (
            "rating",
            "text",
            )
        

class PageAddHostForm(forms.ModelForm):
    
    class Meta:
        model = PageHost
        fields = (
            "host",
            )



class PageClaimForm(forms.ModelForm):
    
    class Meta:
        model = ClaimPage
        fields = (
            "name",
            "email",
            "phone",
            "reason",
            )
        
