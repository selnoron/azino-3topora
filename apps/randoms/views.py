import random

from django.shortcuts import render, redirect
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse


class RandomView(View):
    massive = [ 0, 32, 15, 19, 4, 21, 2, 25, 17, 
                34, 6, 27, 13, 36, 11, 30, 8, 23, 
                10, 5, 24, 16, 33, 1, 20, 14, 31, 
                9, 22,18, 29, 7, 28, 12, 35, 3, 26
                ]
    number = 'Start'
    
    def get(
        self, request: HttpRequest
    ) -> HttpResponse:
        return render(
            request=request,
            template_name="random/wheel.html",
            context={
                'number': self.number,
                'vybor': self.massive
            }
        )


    def post(
        self, request: HttpRequest
    ) -> HttpRequest:
        data = request.POST
        self.number = random.choice(self.massive)
        if data.get('ch') != self.number:
            return redirect('/random/result/bad')
        else:
            return redirect('/random/result/good')

def good_result(request):
    if request.method == "GET":
        return HttpResponse('<h1>!!!Congratulations!!!</h1> <form action="/random/result/good" method="post"> <input type="submit" value="Thanks!!"/> </form>')
    
    return redirect('/random')


def bad_result(request):
    if request.method == "GET":
        return HttpResponse('<h1>!!!Loooooser!!!</h1> <form action="/random/result/bad" method="post"> <input type="submit" value="Thanks!!"/> </form>')
    
    return redirect('/random')