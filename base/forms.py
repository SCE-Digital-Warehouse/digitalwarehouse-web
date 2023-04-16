from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="שם משתמש/ת", widget=forms.TextInput())
    password = forms.CharField(label="סיסמה", widget=forms.PasswordInput())

    def __init__(self, request: None, *args, **kwargs) -> None:
        super().__init__(request, *args, **kwargs)
        self.error_messages["invalid_login"] = (
            "שם משתמש/ת ו/או סיסמה לא נכונים")
