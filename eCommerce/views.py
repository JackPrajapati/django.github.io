from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, get_user_model,logout as log_out
from .forms import ContactForm, LoginForm, RegisterForm
from products.views import product_list
from products.models import Product
from django.db.models import Q
from django.contrib.auth.decorators import login_required



User = get_user_model()


def home_page(request):
	queryset = Product.objects.all()
	context = {
		"title": "Hello Django" ,
		"premium : ": "Yes",
		"qs": queryset
	}
	if request.user.is_authenticated():
		context["premium"] = "Yes"
	return render(request,"home.html",context)


@login_required
def setting_page(request):
	if request.user.is_authenticated():
		context = {
			'title': "Settings" 
		}
		return render(request,"base.html",context)
	else:
		context = {
			'title': "Login Please ..." 
		}
		return redirect("accounts/login.html",context)		


def about_page(request):
	context = {
		"title": "About us" 
	}
	print(context)
	return render(request,"base.html",context)


@login_required
def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title": "Contact us", 
		"form" : contact_form
	}
	# if contact_form.is_valid():
	# if request.method == "POST":
		# print(request.POST.get('fullname'))
		# print(request.POST.get('email'))	
		# print(request.POST.get('content'))	
	return render(request,"contact/view.html",context)


@login_required
def search(request):
	if request.POST:
		q = request.POST.get('q')
		results = Product.objects.filter(  
			Q( title__icontains = q ) |
			Q( price__icontains = q ) |
			Q( description__icontains = q ) )   
		if results:            
			context = {
            	'result' : results,
            	'title' : "Search results for : ",
            	'q' : q.capitalize() ,

            }
			return render(request, "result.html", context)
		else:
			context = {
				'title' : "Nothing found !!!",
			}
			return render(request, "result.html", context)
	else:
		context = {
			'title' : "Invalid search Query !!! ",
		}
		return render(request, "result.html", context)

