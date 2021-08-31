from django import forms


class SentForm(forms.Form):
	name = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name*'}))
	email = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email*'}))
	subject = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Subject*'}))
	message = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 8, 'cols': 100,'placeholder': 'Message*'}))


#
# from django import forms
#
# FRUIT_CHOICES= [
#     ('orange', 'Oranges'),
#     ('cantaloupe', 'Cantaloupes'),
#     ('mango', 'Mangoes'),
#     ('honeydew', 'Honeydews'),
#     ]
#
# class UserForm(forms.Form):
#     first_name= forms.CharField(max_length=100)
#     last_name= forms.CharField(max_length=100)
#     email= forms.EmailField()
#     age= forms.IntegerField()
#     favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES))