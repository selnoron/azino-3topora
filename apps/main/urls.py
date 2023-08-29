from django.urls import path, include
from django.contrib import admin
from main.views import main_page
from randoms.viewes.random_view import RandomView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', main_page, name='main'),
    path('random/',RandomView.as_view(), name='random')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)