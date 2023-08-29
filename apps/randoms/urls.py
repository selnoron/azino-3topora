from django.urls import path

from randoms.viewes.wheel import Wheel, GoodResult, BadResult
from randoms.viewes.random_view import RandomView


urlpatterns = [
    path('', RandomView.as_view()),
    path('wheel/result/good/', GoodResult.as_view()),
    path('wheel/result/bad/', BadResult.as_view())
]