from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password1", "password2")


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            "bio",
            "date_of_birth",
            "profile_picture",
            "phone_number",
            "preparation_time",
        ]

        widgets = {
            "username": forms.TextInput(
                attrs={"style": "resize: none; height: 50px;"}),

            "email": forms.EmailInput
            (attrs={"style": "resize: none; height: 50px;"}),

            "bio": forms.TextInput(
                attrs={"style": "resize: none; height: 50px;"}),

            "date_of_birth": forms.widgets.DateInput(
                format=('%Y-%m-%d'),
                attrs={"type": "date", "style": "resize: none; height: 50px;"}
            ),
            "phone_number": forms.TextInput(
                attrs={"style": "resize: none; height: 50px;"}),

            "preparation_time": forms.TextInput(
                attrs={"style": "resize: none; height: 50px;"}
            ),

            "profile_picture": forms.FileInput(
                attrs={"class": "form-control"}),
        }
