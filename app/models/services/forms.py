from django import forms

from django.forms import ModelForm
from .models import Experience, Event, User

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ['title', 'description', 'datetime', 'price', 'createdBy']

class EventFormUpdate(ModelForm):
	class Meta:
		model = Event
		fields = ['title', 'description', 'datetime', 'price', 'experience']

class ExperienceForm(ModelForm):
	class Meta:
		model = Experience
		fields = ['title', 'description', 'totalPrice']

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['firstName', 'lastName', 'username', 'password']

class UserFormUpdateExperience(forms.Form):
	exp_id = forms.CharField(max_length = 1000000)
	remove = forms.CharField(max_length=10)

class UserFormUpdateEvent(forms.Form):
	event_id = forms.CharField(max_length = 1000000)
	remove = forms.CharField(max_length=10)

class UserFormUpdateFriend(forms.Form):
	user_id = forms.CharField(max_length = 1000000)
	remove = forms.CharField(max_length=10)

class UserFormCheckUser(ModelForm):
	class Meta:
		model = User
		fields = ['username','password']