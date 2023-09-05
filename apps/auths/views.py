from django.shortcuts import render, redirect
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
import json
from auths.forms.register_form import RegisterForm
from auths.forms.login_form import LoginForm
from auths.modelss.my_user import MyUser
from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from auths.forms.register_form import RegisterForm
from auths.forms.login_form import LoginForm
from auths.modelss.my_user import MyUser, Transaction


class RegisterView(View):
    """User Login"""

    template_name = 'register.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form': form
            }
        )
    
    def post(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['password2']
            MyUser.objects.create(**form.cleaned_data)
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form': form
            }
        )
    

class AuthorizView(View):
    """User Login"""

    template_name = 'login.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form': form
            }
        )
    
    def post(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = MyUser.objects.filter(email = form.cleaned_data['email'], password = form.cleaned_data['password'])[0]
            user = user.id
            request.session['user_id'] = user
            return redirect('/auth/user')
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form': form
            }
        )
    

class UserProfile(View):

    template_name = 'profile.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        user = MyUser.objects.get(id = request.session['user_id'])
        trans = Transaction.objects.filter(user = user)
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'user': user,
                'trans': trans
            }
        )
    
    def post(self, request: HttpRequest) -> HttpResponse:
        ...
    
