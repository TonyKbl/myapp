from django import forms
from .models import Profile, LookingFor, Interest
from gallery.models import UserGallery
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class SetProfileTypeForm(forms.ModelForm):
    
    class Meta:        
        model = Profile
        fields = (
            "profile_type",
        )
        help_texts = {
            'profile_type': "Select the profile type you wish to setup",
        }


class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:        
        model = Profile
        fields = (
            "display_name",
            "intro", 
            "description", 
            "location", 
            "outer_postcode",
            "name",
            "DOB",
            "sexuality",
            "height",
            "body_type",
            "smoke",
            "drink",
            )
        
        labels = {
            'display_name': "Enter the name that you want to be displayed on your posts and profile",
            'intro': "Add a short paragraph that appears in bold at the top of your bio",
            'description': "Your main bio",
            'location': "Enter a rough location, Town, City, or County",
            'outer_postcode': "Enter the first part of your postcode, e.g. AB12. Only you can see this",
        }

        widgets = {
            'display_name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'intro': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'outer_postcode': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'DOB': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sexuality': forms.Select(attrs={'class': 'form-control'}),
            'height': forms.Select(attrs={'class': 'form-control'}),
            'body_type': forms.Select(attrs={'class': 'form-control'}),
            'smoke': forms.Select(attrs={'class': 'form-control'}),
            'drink': forms.Select(attrs={'class': 'form-control'}),
        }


class LookingForUpdateForm(forms.ModelForm):
    
    class Meta:        
        model = LookingFor
        fields = (
            "age_min",
            "age_max", 
            "men", 
            "women", 
            "mf_couple",
            "ff_couple",
            "mm_couple",
            "cd_tv",
            "tg_ts",
            "can_accom",
            "can_travel",
            "smokers",
            )


class InterestUpdateForm(forms.ModelForm):
    
    class Meta:        
        model = Interest
        fields = '__all__'

class Profile2ndPersonForm(forms.ModelForm):
    
    class Meta:        
        model = Profile
        fields = (            
            "name2",
            "DOB2",
            "sexuality2",
            "height2",
            "body_type2",
            "smoke2",
            "drink2",
            )
        
        labels = {
            'name2':"Name - Person 2 (Couples Only)",
            'DOB2':"DOB - Person 2 (Couples Only)",
            'sexuality2':"Sexuality - Person 2 (Couples Only)",
            'height2':"Name - Person 2 (Couples Only)",
            'body_type2':"Body Type - Person 2 (Couples Only)",
            'smoke2':"Smoke - Person 2 (Couples Only)",
            'drink2':"Drink - Person 2 (Couples Only)",

        }
        
        widgets = {
            'name2': forms.TextInput(attrs={'class': 'form-control'}),
            'DOB2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sexuality2': forms.Select(attrs={'class': 'form-control'}),
            'height2': forms.Select(attrs={'class': 'form-control'}),
            'body_type2': forms.Select(attrs={'class': 'form-control'}),
            'smoke2': forms.Select(attrs={'class': 'form-control'}),
            'drink2': forms.Select(attrs={'class': 'form-control'}),
        }

        def __str__(self):
            return self.user
        
        # def form_valid(self, form):
        #     form.instance.lat = 'tony'
        #     form.instance.lon = 'keeble'
        #     coords = super().form_valid(form)
        #     print(coords)
        #     return coords
        
class ProfileCoverUpdateForm(forms.ModelForm):
    
    class Meta:        
        model = Profile
        fields = (
            "cover_image",
        )

        def __str__(self):
            return self.user
        
class ProfileAvatarUpdateForm(forms.ModelForm):
    
    class Meta:        
        model = Profile
        fields = (
            "image",
        )

        def __str__(self):
            return self.user
        

class ProfileGalleryCreateForm(forms.ModelForm):
    
    class Meta:        
        model = UserGallery
        fields = (
            "image",
            "private",
        )

        def __str__(self):
            return self.user