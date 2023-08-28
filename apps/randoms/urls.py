from django.urls import path

from randoms.views import RandomView, GoodResult, BadResult
from . import views


urlpatterns = [
    path('', RandomView.as_view()),
    path('result/good/', GoodResult.as_view()),
    path('result/bad/', BadResult.as_view())
]