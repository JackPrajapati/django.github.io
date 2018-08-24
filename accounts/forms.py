from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Profile

class LoginForm(forms.Form):
	username = forms.CharField(label= "Username",widget=forms.TextInput(
			attrs={
					"class": "form-control", 
					"id": "form_username", 
				}
			),required=False
		)
	password = forms.CharField(label= "Password",widget=forms.PasswordInput(
			attrs={
					"class": "form-control", 
					"id": "form_password", 
				}
			),required=False
		)

User = get_user_model()
class RegisterForm(forms.Form):
	username = forms.CharField(label= "Username",widget=forms.TextInput(
			attrs={
					"class": "form-control", 
					"id": "form_username", 
					# "placeholder": "Username "
				}
			),required=False
		)
	email = forms.EmailField(label= "Email",widget=forms.EmailInput(
		attrs={
				"class": "form-control", 
				"id": "from_email",
				# "placeholder": "Your Email"
				}
			),required=False
		)
	password = forms.CharField(widget=forms.PasswordInput(
			attrs={
					"class": "form-control", 
					"id": "form_password", 
					# "placeholder": "Password "
				}
			),required=False, label= "Password"
		)
	password2 = forms.CharField(widget=forms.PasswordInput(
			attrs={
					"class": "form-control", 
					"id": "form_password2", 
					# "placeholder": "Conferm Password "
				}
			),required=False, label= "Conferm Password"
		)

	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username is already taken.")
		return username

	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("Email is already taken.")
		return email

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password2 != password:
			raise forms.ValidationError("Password must match.")
		else:
			return data