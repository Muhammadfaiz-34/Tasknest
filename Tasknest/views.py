from django.views.generic import TemplateView
from django.shortcuts import render, redirect


class home(TemplateView):
    template_name = 'home.html'