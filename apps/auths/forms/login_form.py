from django import forms

from auths.modelss.my_user import MyUser

class LoginForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = (
            'email',
            'password'
        )