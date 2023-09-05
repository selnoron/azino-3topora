from django import forms
from typing import Any, Dict
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
        max_length=200,
        label='email'
    )
    nickname = forms.CharField(
        max_length=100,
        label='your nickname'
       
    )
    password = forms.CharField(
        min_length=6,
        label='password'
    )
    password2 = forms.CharField(
        min_length=6,
        label='repeat password'
    )

    def clean(self) -> Dict[str, Any]:
        return super().clean()
    
    def clean_password2(self) -> Dict[str, Any]:
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise ValidationError()
        return self.cleaned_data