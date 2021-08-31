from django.forms import ModelForm
from .models import Post
from django import forms
from phonenumber_field.modelfields import PhoneNumberField

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content']

class SentForm(forms.Form):
	name = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name*'}))
	email = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email*'}))
	phone= forms.CharField(max_length=80,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Phone*'}))
	subject = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Subject*'}))
	message = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control','rows': 6, 'placeholder': 'Message*'}))

class Subscribe(forms.Form):
	Email = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control','style':'width:300.988636px;','placeholder':'Enter your email*'}))

	def __init__(self, *args, **kwargs):
		super(Subscribe, self).__init__(*args, **kwargs)
		self.fields['Email'].label = ""




class DemoForm(forms.Form):
    name = forms.CharField(initial='Your Name', max_length=100,label=False)
    company = forms.CharField(initial='Company Name', max_length=100,label=False)
    email = forms.EmailField(initial='Email',label=False)
    phone = forms.CharField(initial='Phone Number', max_length=100,label=False)