from django.urls import path

from randoms.views import RandomView, good_result, bad_result
from . import views


urlpatterns = [
    path('', RandomView.as_view()),
    path('result/good', views.good_result),
    path('result/bad', views.bad_result)
]