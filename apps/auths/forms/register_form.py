from django import forms


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