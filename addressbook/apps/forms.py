from django import forms

class adddetailform(forms.Form):
	
	name = 			forms.CharField(widget=forms.TextInput())
	dateofbirth = 	forms.CharField(widget=forms.TextInput())
	address = 		forms.CharField(widget=forms.TextInput())
	phone_number =  forms.CharField(widget=forms.TextInput())
	email = 		forms.EmailField(widget=forms.TextInput())
	state = 		forms.CharField(widget=forms.TextInput())
	country = 		forms.CharField(widget=forms.TextInput())
	
	def clean(self):
		return self.cleaned_data
