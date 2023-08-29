import random

from django.shortcuts import render, redirect
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse


class RandomView(View):

    def get(
        self, request: HttpRequest
    ) -> HttpResponse:
        return render(
            request=request,
            template_name="random/wheel.html",
            context={
            }
        )
