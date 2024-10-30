from django import forms
from .models import Meeting
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


# class MeetingCreateForm(forms.ModelForm):
#     class Meta:
#         model = Meeting
#         fields = ['agenda']
#         widgets = {
#             'agenda': forms.Textarea(attrs={'rows': 12,
#                                             "style": "resize: none"}),
#         }


class MeetingEditForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'agenda', 'status', 'participants']
        widgets = {
            'title': forms.TextInput(attrs={'id': 'title'}),
            'agenda': forms.Textarea(attrs={'id': 'agenda'}),
            'status': forms.Select(attrs={'id': 'status'}),
            'participants': forms.TextInput(attrs={'id': 'participants'}),
        }


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'participants', 'date_time', 'status', 'agenda']


class MeetingCreateForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'agenda']