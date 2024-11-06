from django import forms
from .models import Page, PageReviews, ClaimPage, PageHost, ClubPage, HotelPage
from django.contrib.auth.models import User


# class PageCreateForm(forms.ModelForm):
#     class Meta:
#         model = Page
#         fields = (
#             "page_type",
#             "page_name",
#             "address1",
#             "address2",
#             "town_city",
#             "county",
#             "post_code",
#             "description",
#         )

#         def __str__(self):
#             return self.model.page


# class PageUpdateForm(forms.ModelForm):
# class Meta:
#     model = Page
#     fields = (
#         "page_type",
#         "page_name",
#         "address1",
#         "address2",
#         "town_city",
#         "county",
#         "post_code",
#         "region",
#         "description",
#     )


class ClubPageCreateForm(forms.ModelForm):
    class Meta:
        model = ClubPage
        fields = (
            "page_name",
            "address1",
            "address2",
            "town_city",
            "county",
            "post_code",
            "region",
            "description",
            "phone_number",
            "show_phone_button",
            "email",
            "show_email_button",
        )

        def __str__(self):
            return self.model.page


class ClubPageUpdateForm(forms.ModelForm):
    class Meta:
        model = ClubPage
        fields = (
            "address1",
            "address2",
            "town_city",
            "county",
            "post_code",
            "region",
            "description",
            "phone_number",
            "show_phone_button",
            "email",
            "show_email_button",
        )


class HotelPageCreateForm(forms.ModelForm):
    class Meta:
        model = HotelPage
        fields = (
            "page_name",
            "address1",
            "address2",
            "town_city",
            "county",
            "post_code",
            "region",
            "description",
            "phone_number",
            "show_phone_button",
            "email",
            "show_email_button",
            "num_rooms",
            "ensuite",
        )

        def __str__(self):
            return self.model.page


class HotelPageUpdateForm(forms.ModelForm):
    class Meta:
        model = HotelPage
        fields = (
            "address1",
            "address2",
            "town_city",
            "county",
            "post_code",
            "region",
            "description",
            "phone_number",
            "show_phone_button",
            "email",
            "show_email_button",
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
        fields = ("host",)


class PageClaimForm(forms.ModelForm):
    class Meta:
        model = ClaimPage
        fields = (
            "name",
            "email",
            "phone",
            "reason",
        )


class PageEmailForm(forms.Form):
    full_name = forms.CharField(max_length=20)
    email = forms.CharField(max_length=30)
    subject = forms.CharField(max_length=50)
    message = forms.CharField(max_length=500)

    class Meta:
        fields = ["name", "email", "subject", "message"]
