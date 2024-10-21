from django import forms
from .models import ClubEvent
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
