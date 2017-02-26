from django import forms

from django.forms import ModelForm
from .models import Experience, Event, User

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ['title', 'description', 'datetime', 'price']

class ExperienceForm(ModelForm):
	class Meta:
		model = Experience
		fields = ['title', 'description', 'totalPrice']

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