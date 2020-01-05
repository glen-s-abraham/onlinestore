from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserDetails
from .forms import UserForm,UserDetailsForm
# Create your views here.
def register(request):
	registered=False
	user_form=UserForm()
	userdetails_form=UserDetailsForm()
	if request.method=="POST":
		userform=UserForm(request.POST)
		userdetailsform=UserDetailsForm(request.POST)
		if userform.is_valid() and userdetailsform.is_valid():
			user=userform.save()
			userdetailsform=UserDetailsForm(request.POST)
			userdetails=userdetailsform.save(commit=False)
			userdetails.user=user

			print(userdetails.user)
			userdetails.save()
			registered=True


		
		
		
	context={'user_form':user_form,'userdetails_form':userdetails_form,'registered':registered}
	return render(request,'user/register.html',context)

def login(request):
	return render(request,'user/login.html')