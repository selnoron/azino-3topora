from django import forms

from auths.modelss.my_user import MyUser
from django.core.exceptions import ValidationError, FieldError
from typing import Any, Dict


class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=200,
        label='email'
    )
    password = forms.CharField(
        min_length=6,
        label='password'
    )
    def clean(self) -> Dict[str, Any]:         
        email = self.cleaned_data['email']         
        password = self.cleaned_data['password']         
        if MyUser.objects.filter(email=email, password=password).exists():             
            return self.cleaned_data                  
        raise ValidationError('не совпадают логин и пароль')