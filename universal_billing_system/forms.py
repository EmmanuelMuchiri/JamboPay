from django import forms	
from .models import *
from django.contrib.auth.models import User	
# from django.contrib.auth.forms import MerchanLoginForm
# from django.contrib.auth.forms import MerchantLoginForm
# from django.contrib.auth.models import Merchant

# sign up forms
class LoginForm():
   	email = forms.EmailField(max_length=200, help_text='Required')
   	class Meta:
   	        model = Merchant
         
# class SignupForm():
#     email = forms.EmailField(max_length=200, help_text='Required')
#     class Meta:
#         model = Merchant
#         fields = ('username', 'email', 'password1', 'password2')
        


class BillsForm(forms.ModelForm):
    class Meta:
        model = Bills
        fields = '__all__'
        widgets = {
            'Revstreams': forms.CheckboxSelectMultiple(),
        }
        exclude = ['status','generated_by']

class NoteForm(forms.ModelForm):
    class Meta:
        model = BillRecipients
        fields = '__all__'

class NewsLetterForm(forms.Form):
    customer_name = forms.CharField(label="First Name",max_length=30)
    customer_email = forms.EmailField(label="Enter your Email Address")


class EmailForm(forms.Form):
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    botcheck = forms.CharField(max_length=5)
    message = forms.CharField()
