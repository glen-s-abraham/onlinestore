from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserDetails

class UserForm(UserCreationForm):
	email=forms.EmailField()
	class Meta():
		model=User
		fields=('username','email','password1','password2')
class UserDetailsForm(forms.ModelForm):
	class Meta():
		model=UserDetails
		fields=('mobile','address')