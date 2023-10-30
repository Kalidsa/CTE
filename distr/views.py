from django.shortcuts import render
from django.http import HttpResponse

def base(request):
    return render(request, 'base/base.html')

def login(request):
    return render(request, 'base/login.html')
      
