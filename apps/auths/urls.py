from django.urls import path
from auths.views import RegisterView, AuthorizView, UserProfile


urlpatterns = [
    path('reg/', RegisterView.as_view()),
    path('log/', AuthorizView.as_view()),
    path('user/', UserProfile.as_view())
]