from django import forms

class CreateEventForm(forms.Form):
	title = forms.CharField(
		label="Title", 
		max_length=200, 
		widget=forms.TextInput(
			attrs={
			'class':'form-control', 
			'placeholder': 'Enter a title for your event.'
			}))

	date = forms.DateField(
		label="Date",
		widget=forms.DateInput(
			attrs={
			'class':'form-control',
			'type' : 'date'
			}))

	time = forms.TimeField(
		label="Time",
		widget=forms.TimeInput(
			attrs={
			'class':'form-control',
			'type' : 'time'
			}))

	price = forms.DecimalField(
		label="Price", 
		max_digits=6, 
		decimal_places=2,
		widget=forms.NumberInput(
			attrs={
			'class' : 'form-control',
			'type' : 'number',
			'placeholder' : '0.00'
			}))

	description = forms.CharField(
		label="Description", 
		max_length=400,
		widget=forms.Textarea(
			attrs={
			'class':'form-control', 
			'placeholder': 'Describe your event.',
			'rows':'3'
			}))