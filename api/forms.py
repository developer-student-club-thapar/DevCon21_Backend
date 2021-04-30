from django import forms

from api.models import Participant


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        exclude = ("id",)
