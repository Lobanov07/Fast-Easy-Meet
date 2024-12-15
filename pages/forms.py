from django import forms
from .models import Meeting, Schedule

from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class MeetingEditForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'status', 'agenda', 'preferred_date']
        widgets = {
                "preferred_date": forms.widgets.DateInput(
                format=('%Y-%m-%d'),
                attrs={"type": "date", "style": "resize: none; height: 50px;"}
            ),
           }


class MeetingCreateForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'agenda', 'preferred_date']
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['start_time', 'end_time', 'description']
        widgets = {
            'description': forms.Textarea(
                attrs={"style": "resize: none; height: 100px; wigth: 200px; border-radius: 10px; border: 2px solid black; display: inline-block; vertical-align: top;"}),
            'start_time': forms.DateTimeInput(
                attrs={'type': 'datetime-local', "style": "border-radius: 10px"}),
            'end_time': forms.DateTimeInput(
                attrs={'type': 'datetime-local', "style": "border-radius: 10px"}),
        }
