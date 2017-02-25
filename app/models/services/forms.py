from django import forms

class EventForm(forms.Form):
	datetime = forms.DateTimeField()
	price = forms.DecimalField(max_digits=6, decimal_places=2)
	title = forms.CharField(max_length=200)
	description = forms.CharField(max_length=400)

class ExperienceForm(forms.Form):
	title = forms.CharField(max_length = 200)
	description = forms.CharField(max_length = 400)
	totalPrice = forms.DecimalField(max_digits = 8, decimal_places=2)

class UserFormCreate(forms.Form):
	firstName = forms.CharField(max_length=20)
	lastName = forms.CharField(max_length=20)
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=50)

class UserFormUpdateUser(forms.Form):
	firstName = forms.CharField(max_length=20)
	lastName = forms.CharField(max_length=20)
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=50)

class UserFormUpdateExperience(forms.Form):
	exp_id = forms.CharField(max_length = 1000000)
	remove = forms.CharField(max_length=10)

class UserFormUpdateEvent(forms.Form):
	event_id = forms.CharField(max_length = 1000000)
	remove = forms.CharField(max_length=10)

class UserFormUpdateFriend(forms.Form):
	user_id = forms.CharField(max_length = 1000000)
	remove = forms.CharField(max_length=10)