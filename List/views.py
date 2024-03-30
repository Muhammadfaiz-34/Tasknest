from django.shortcuts import render, redirect 
from django.views.generic import TemplateView
from User.views import *
from User.forms import *


def home (request):
    return render(request, 'home.html')

def login (request):
    form = SignUpForm() 
    return render(request,  'signup.html', {'form': form})

def signup (request):
    form = SignInView() 
    return render(request,  'login.html', {'form': form})
    
