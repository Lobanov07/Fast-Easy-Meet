from django import forms
from .models import Meeting
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['agenda']
        widgets = {
            'agenda': forms.Textarea(attrs={'rows': 12,
                                            "style": "resize: none"}),
        }
