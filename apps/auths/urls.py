from django.urls import path
from auths.views import RegisterView


urlpatterns = [
    path('reg/', RegisterView.as_view())
]