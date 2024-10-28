from django import forms
from .models import Meeting
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class MeetingCreateForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['agenda']
        widgets = {
            'agenda': forms.Textarea(attrs={'rows': 12,
                                            "style": "resize: none"}),
        }


class MeetingEditForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['date_time', 'status', 'agenda', 'participants']
        widgets = {
            'agenda': forms.Textarea(attrs={'rows': 10, 'cols': 80, 'class': 'form-control', 'placeholder': 'Введите повестку встречи...'}),
            'date_time': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Выберите дату и время...'}),
            'participants': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите участников встречи...'}),
        }