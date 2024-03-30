from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class Project(TemplateView):
    template_name = 'project.html'
    
