from django.shortcuts import render
from django.utils import timezone

def homepage(request):
    return render(request, 'mysite/homepage.html')
