from django import forms
from typing import Any, Dict
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='email',
        max_length=200
    )
    nickname = forms.CharField(
        ladel='your nickname',
        max_length=100
    )
    password = forms.CharField(
        label='password',
        min_length=6
    )
    password2 = forms.CharField(
        label='repeat password',
        min_length=6
    )

    def clean(self) -> Dict[str, Any]:
        return super().clean()
    
    def clean_password(self) -> Dict[str, Any]:
        if self.cleaned_data['password'] != self.changed_data['password2']:
            raise ValidationError()