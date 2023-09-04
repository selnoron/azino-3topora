from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from auths.forms.register_form import RegisterForm


class LoginView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        ...

    def post(self, request: HttpRequest) -> HttpResponse:
        ...

class RegisterView(View):

    template_name = 'register.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm()
        return render(
            request=request,
            template_name=self.template_name,
            context={
            }
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm()
        form.is_valid()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form': form
            }
        )