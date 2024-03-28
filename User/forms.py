from django import forms 
from django.contrib.auth.forms import UserCreationForm
from User.models import user_m

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    class meta:
        model = user_m 
        fields = ['id', 'username', 'Email', 'role','owner_id', 'picture']
        
class SignInForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


        

    
