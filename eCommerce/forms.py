from django import forms
from django.contrib.auth import get_user_model
# from .models import ContactModel

class ContactForm(forms.Form):

	fullname = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class": "form-control",
				"id": "form_fullname",
				"placeholder": "Your Fullname "
			}
		)
	)
	email = forms.EmailField(
	widget=forms.EmailInput(
		attrs={
				"class": "form-control", 
				"id": "from_email",
				"placeholder": "Your Email"
				}
			)
		)
	content = forms.CharField(
		widget=forms.Textarea(
			attrs={
					"class": "form-control", 
					"id": "form_content", 
					"cols": "10",
					"placeholder": "Your Message... "
				}
			)
		)

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if not ("gmail.com" or "yahoo.com" or "hotmail.com") in email:
			raise forms.ValidationError("Email must be gmail.com, yahoo.com or hotmail.com")
		return email
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
		# return data

	# class Meta:
	# 	fullname = forms.CharField(
	# 		widget=froms.TextInput(
	# 			attrs={
	# 				"class": "form-control",
	# 				"id": "fullname",
	# 				"placeholder": "Your fullname"
	# 			}
	# 		)
	# 	)
	# 	email = forms.CharField(
	# 		widget=froms.EmailInput(
	# 			attrs={
	# 				"class": "form-control",
	# 				"id": "email",
	# 				"placeholder": "Your email"
	# 			}
	# 		)
	# 	)
	# 	content = forms.CharField(
	# 		widget=froms.Textarea(
	# 			attrs={
	# 				"class": "form-control",
	# 				"id": "content",
	# 				"placeholder": "Your Message..."
	# 			}
	# 		)
	# 	)
	# 	model = ContactModel
	# 	CharField = {'fullname', 'email', 'content'}