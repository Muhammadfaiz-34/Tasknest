from django.urls import path 
from Board.views import *

urlpatterns = [
    path('create/', Project.as_view()),
]