"""MAIN APP"""

from django.shortcuts import render

def main_page(request):
    return render(
        template_name='main.html',
        request=request
    )