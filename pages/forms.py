from django import forms
from .models import Meeting, Schedule

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


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['start_time', 'end_time', 'description']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }