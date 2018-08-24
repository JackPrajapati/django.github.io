from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, get_user_model,logout as log_out
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from products.models import Product

User = get_user_model()


@login_required
def profile_page(request):
	print(yessssssssssssssssssssss)
	form = RegisterForm()
	context = {
		'title': "My Profile" ,
		'form' : form
	}
	return render(request,"base.html",context)

def login_page(request):
	form = LoginForm(request.POST)
	context = {
		"title": "Login Here ",
		"form": form, 
	}
	# print("User Logged In")
	# print(request.user.is_authenticated())
	if request.user.is_authenticated:
		queryset = Product.objects.all()
		context = {'title' : "Welcome , " + request.user.username.capitalize(), 'qs' : queryset} 
		return render(request,"home.html",context)
	elif form.is_valid():
		# print(request.user.is_authenticated())
		# print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username = username, password = password)
		if user is not None:	
			# print(request.user.is_authenticated())
			# print(user)
			login(request,user)
			queryset = Product.objects.all()
			context = {'title' : "Welcome , " + request.user.username.capitalize(), 'qs' : queryset}
			return render(request,"home.html",context)
			# redirect to success page
			# context['form'] = LoginForm()
		else:
			# return error
			print("Error")
	return render(request,"accounts/login.html",context)


def register_page(request):
	if request.POST:
		form = RegisterForm(request.POST)
		context = {
			"title": "Register Here " ,
			"form": form, 
		}
		if form.is_valid():
			print(form.cleaned_data)
			username = form.cleaned_data.get("username")
			email = form.cleaned_data.get("email")
			password = form.cleaned_data.get("password")
			new_user = User.objects.create_user(username, email, password)
			print(new_user)
		return render(request,"accounts/register.html",context)
	elif request.user.is_authenticated():
		return render(request,"base.html",context)
	else:
		form = RegisterForm()
		context = {
			"title": "Register Here " ,
			"form": form, 
		}
		return render(request,"accounts/register.html",context)

def logout_page(request):
	log_out(request)
	form = LoginForm(request.POST)
	context = {
		"title": "Login Here ",
		"form": form, 
	}
	return render(request,"accounts/login.html",context)