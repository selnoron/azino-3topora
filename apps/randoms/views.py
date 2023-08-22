import random

from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse


class RandomView(View):
    massive = [ 0, 32, 15, 19, 4, 21, 2, 25, 17, 
                34, 6, 27, 13, 36, 11, 30, 8, 23, 
                10, 5, 24, 16, 33, 1, 20, 14, 31, 
                9, 22,18, 29, 7, 28, 12, 35, 3, 26
                ]
    
    def get(
        self, request: HttpRequest
    ) -> HttpResponse:
        return render(
            request=request,
            template_name="random/wheel.html",
            context={
                'vybor': self.massive,
                'rng': range(len(self.massive))
            }
        )


    def post(
        self, request: HttpRequest
    ) -> HttpResponse:
        
        return render(
            request=request,
            template_name="random/wheel.html",
            context={
                'number': random.choise(RandomView.massive),
                'vybor': RandomView.massive,
                'len': range(len(RandomView.massive))
            }
        )
