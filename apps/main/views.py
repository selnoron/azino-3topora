from django.shortcuts import render
from randoms.models import Banner

def main_page(request):
    return render(
        template_name='main.html',
        request=request
    )
