from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignUpForm 
from .forms import SignInForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect ('login')  
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form, 'error_message': 'Either wrong password or gmail'})

class SignInView(TemplateView):
    template_name = 'login.html'

    def post(self, request):
        form = SignInForm(request.get)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home.html')  
            else:
                
                return render(request, 'home.html', {'form': form, 'error_message': 'Invalid username or password.'})
        else:
            
            return render(request, 'signup.html', {'form': form})
    
    def get(self, request):
        form = SignInForm()
        return render(request, 'login.html', {'form': form})

class home (TemplateView):
    template_name = 'home.html'


    
    
