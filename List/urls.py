from django.urls import path 
from List.views import *

urlpatterns = [
    path('land/', home, name='login' ),
    path ('land/login', login),
    path ('land/signup', signup)
]