from django.urls import path 
from User.views import *

urlpatterns = [
    path('signup/', signup),
    path('signin/', SignInView.as_view()),
]

