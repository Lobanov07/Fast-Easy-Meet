from django import forms
from .models import Meeting
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class MeetingEditForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'status', 'agenda']


class MeetingCreateForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'agenda']
