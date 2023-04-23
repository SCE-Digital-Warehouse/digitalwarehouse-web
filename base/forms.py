from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordResetForm, PasswordChangeForm

User = get_user_model()


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="שם משתמש/ת",
        widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label="סיסמה",
        strip=False,
        widget=forms.PasswordInput())

    def __init__(self, request: None, *args, **kwargs) -> None:
        super().__init__(request, *args, **kwargs)
        self.error_messages["invalid_login"] = (
            "שם משתמש/ת ו/או סיסמה לא נכונים")

    def change_password_is_required(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        identity_num = User.objects.filter(
            username=username).values_list("identity_num", flat=True).first()
        if password == identity_num:
            return True
        return False


class PasswordSetForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="בחר/י סיסמה חדשה",
        strip=False,
        widget=forms.PasswordInput(attrs={"autofocus": True}),
        help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(
        label="אמת/י את הסיסמה",
        strip=False,
        widget=forms.PasswordInput())


class ResetPasswordFrom(PasswordResetForm):
    email = forms.EmailField(
        label=("מייל"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autofocus": True}),
    )
