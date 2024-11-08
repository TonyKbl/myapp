from django import forms
from .models import ClubEvent, Guestlist, Event, Meet
from pages.models import Page, PageHost
from django.contrib.auth.models import User


# uncomment after migration
class ClubEventCreateForm(forms.ModelForm):
    # host_list = forms.ModelMultipleChoiceField(
    #     # choices = 'host_choices',
    #     queryset=PageHost.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True)

    class Meta:
        model = ClubEvent
        fields = (
            "title",
            "description",
            "image",
            "ot_men",
            "ot_women",
            "ot_mfcouples",
            "ot_ffcouples",
            "ot_mmcouples",
            "ot_tvts",
            "private",
        )

    def get_context_data(self, *args, **kwargs):
        context = super(ClubEventCreateForm, self).get_context_data(*args, **kwargs)
        context["host_choices"] = PageHost.objects.filter(
            page_name_id=self.kwargs["pk"]
        )
        return context


class PrivateMeetAddForm(forms.ModelForm):
    class Meta:
        model = Meet
        fields = (
            "meet_type",
            "title",
            "Location",
            "description",
            "date",
            "start_time",
            "ot_men",
            "ot_women",
            "ot_mfcouples",
            "ot_ffcouples",
            "ot_mmcouples",
            "ot_tvts",
        )

        widgets = {
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "start_time": forms.TimeInput(
                attrs={"class": "form-control", "type": "time"}
            ),
        }


class GuestlistCreateForm(forms.ModelForm):
    class Meta:
        model = Guestlist
        fields = ("private",)

        class Meta:
            unique_together = (
                "guest",
                "event",
            )


class GuestlistDeleteForm(forms.ModelForm):
    class Meta:
        model = Guestlist
        exclude = (
            "private",
            "event",
            "guest",
            "profile_type",
            "non_member",
        )


class ClubAddNonMemberGuestlistForm(forms.ModelForm):
    class Meta:
        model = Guestlist
        fields = (
            "non_member",
            "profile_type",
            "private",
        )

        class Meta:
            unique_together = (
                "guest",
                "non_member",
                "event",
            )


class EventAddDatesForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            "date",
            "start_time",
            "end_time",
            "admission_fees",
            "additional_info",
        )

        widgets = {
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "start_time": forms.TimeInput(
                attrs={"class": "form-control", "type": "time"}
            ),
            "end_time": forms.TimeInput(
                attrs={"class": "form-control", "type": "time"}
            ),
        }
