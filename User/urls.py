from django.urls import path 
from User.views import *

urlpatterns = [
    path('signup/', signup),
    path('signin/<email><password>', SignInView.as_view()),
    path('home/', home.as_view()),
]

