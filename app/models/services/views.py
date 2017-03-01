from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

import json

from .models import Event, Experience, User
from .forms import EventForm, ExperienceForm, UserForm, UserFormUpdateExperience, UserFormUpdateEvent,UserFormUpdateFriend,EventFormUpdate

# "/" : entry point to Models API
def index(request):
	response_data = {}
	if request.method == 'GET':
		response_data['result'] = '200'
		response_data['message'] = "Successful: Entry point to the Models API."
		return JsonResponse(response_data, safe=False)

# "/event" : list of all events via GET or create an event via POST
def eventAll(request):
	response_data = {}
	events = Event.objects.filter(**request.GET.dict())

	if request.method == 'GET':
		data = serializers.serialize("json", events)
		response_data['result'] = '200'
		response_data['message'] = 'OK: Successful'
		response_data['event_list'] = json.loads(data)
		return JsonResponse(response_data, safe=False)

	if request.method == 'POST':
		form = EventForm(request.POST)

		if form.is_valid():
			e = form.save()
			response_data['result'] = '200'
			response_data['message'] = 'OK: Successful'
			response_data['event'] = json.loads(serializers.serialize("json", [e,]))
			return JsonResponse(response_data, safe = False)
		else:
			response_data['result'] = '400'
			response_data['message'] = 'Bad Request'
			return JsonResponse(response_data, safe = False)

# "/event/<event_id>/" : event by id via GET or event update via POST
def eventById(request, event_id):
	response_data = {}

	try:
		event = Event.objects.get(pk = event_id)
	except ObjectDoesNotExist:
		response_data['result'] = '404'
		response_data['message'] = 'Not Found: Event item not found'
		return JsonResponse(response_data, safe=False)
	else:
		if request.method == 'GET':
			data = serializers.serialize("json", [event,])
			response_data['result'] = '200'
			response_data['message'] = 'OK: Successful'
			response_data['event'] = json.loads(data)
			return JsonResponse(response_data, safe=False)

		if request.method == 'POST':
			form = EventFormUpdate(request.POST, instance=event)

			if form.is_valid():
				e = form.save()
				response_data['result'] = '200'
				response_data['message'] = 'OK: Successful'
				response_data['event'] = json.loads(serializers.serialize("json", [e,]))
				return JsonResponse(response_data, safe = False)
			else:
				response_data['result'] = '400'
				response_data['message'] = 'Bad Request'
				return JsonResponse(response_data, safe = False)


def eventByExpId(request, exp_id):
	response_data = {}
	try:
		event = Event.objects.filter(experience = exp_id)
	except ObjectDoesNotExist:
		response_data['result'] = '404'
		response_data['message'] = 'Not Found: Event item not found'
		return JsonResponse(response_data, safe=False)
	else:
		if request.method == 'GET':
			data = serializers.serialize("json", event)
			response_data['result'] = '200'
			response_data['message'] = 'OK: Successful'
			response_data['event_list'] = json.loads(data)
			return JsonResponse(response_data, safe=False)

		

# "/events/remove/" : event removal by event_id (or ALL) via POST 
def remove(request):
	response_data = {}
	if request.method == 'POST':
		event_id = request.POST["event_id"]
		try:
			event = Event.objects.get(pk = event_id)
		except ObjectDoesNotExist:
			response_data['result'] = '404'
			response_data['message'] = "Not Found: Event item not found"
			return JsonResponse(response_data, safe = False)
		else:
			event.delete()
			response_data['result'] = '200'
			response_data['message'] = 'OK: Successful'
			return JsonResponse(response_data, safe = False)

# "/experience" : list of all experiences via GET or create an event via POST
def experienceAll(request):
	experiences = Experience.objects.filter(**request.GET.dict())

	if request.method == 'GET':
		data = serializers.serialize("json", experiences)
		response_data = {}
		response_data['result'] = '200'
		response_data['message'] = 'OK: Successful'
		response_data['experience'] = json.loads(data)
		return JsonResponse(response_data, safe=False)

	if request.method == 'POST':
		form = ExperienceForm(request.POST)

		if form.is_valid():
			e = form.save()
			response_data = {}
			response_data['result'] = '200'
			response_data['message'] = 'OK: Successful'
			response_data['experience'] = json.loads(serializers.serialize("json", [e,]))
			return JsonResponse(response_data, safe = False)
		else:
			response_data = {}
			response_data['result'] = '400'
			response_data['message'] = 'Bad Request'
			return JsonResponse(response_data, safe = False)

# "/experience/<experience_id>/" : experience by id via GET or experience update via POST
def experienceById(request, exp_id):
	
	try:
		experience = Experience.objects.get(pk=exp_id)
	except ObjectDoesNotExist:
		response_data = {}
		response_data['result'] = '404'
		response_data['message'] = 'Not Found: Experience item not found'
		return JsonResponse(response_data, safe=False)

	else:

		if request.method == 'GET':
			response_data = {}
			response_data['result'] = '200'
			response_data['message'] = 'OK: Successful'
			response_data['experience'] = json.loads(serializers.serialize("json", [experience,]))
			return JsonResponse(response_data, safe=False)

		if request.method == 'POST':
			form = ExperienceForm(request.POST, instance=experience)

			if form.is_valid():
				e = form.save()
				response_data = {}
				response_data['result'] = '200'
				response_data['message'] = 'OK: Successful'
				response_data['experience'] = json.loads(serializers.serialize("json", [e,]))
				return JsonResponse(response_data, safe=False)
			else:
				response_data = {}
				response_data['result'] = '400'
				response_data['message'] = 'Bad Request'
				return JsonResponse(response_data, safe=False)


# "/experience/remove/" : experience removal by experience_id (or ALL) via POST 
def removeExperience(request):

	if request.method == 'POST':
		experience_id = request.POST['experience_id']

		try:
			experience = Experience.objects.get(pk = experience_id)	
		except ObjectDoesNotExist:
			response_data = {}
			response_data['result'] = '404'
			response_data['message'] = "Not Found: Experience item not found"
			return JsonResponse(response_data, safe = False)
		else:
			experience.delete()
			response_data = {}
			response_data['result'] = '200'
			response_data['message'] = 'OK: Successful'
			return JsonResponse(response_data, safe = False)

def userAll(request):
	user = User.objects.filter(**request.GET.dict())

	if request.method == 'GET':
		data = serializers.serialize("json", user)
		return JsonResponse(json.loads(data), safe=False)

	if request.method == 'POST':
		form = UserForm(request.POST)

		if form.is_valid():
			e = form.save()
			response_data = {}
			response_data['result'] = '200'
			response_data['message'] = 'OK: Successful'
			response_data['user'] = json.loads(serializers.serialize("json", [e,]))
			return JsonResponse(response_data, safe = False)
		else:
			response_data = {}
			response_data['result'] = '400'
			response_data['message'] = 'Bad Request'
			return JsonResponse(response_data, safe = False)

def userById(request, user_id):

	try:
		user = User.objects.get(pk = user_id)
	except ObjectDoesNotExist:
		response_data = {}
		response_data['result'] = '404'
		response_data['message'] = 'Not Found: User not found'
		return JsonResponse(response_data, safe=False)
	else:

		if request.method == 'GET':
				data = serializers.serialize("json", [user])
				return JsonResponse(json.loads(data), safe=False)

		if request.method == 'POST':
			form = UserForm(request.POST, instance = user)

			if form.is_valid():
				e = form.save()

				response_data = {}
				response_data['result'] = '200'
				response_data['message'] = 'OK: Successful'
				response_data['user'] = json.loads(serializers.serialize("json", [e,]))
				return JsonResponse(response_data, safe = False)

			else:
				response_data = {}
				response_data['result'] = '400'
				response_data['message'] = 'Bad Request'
				return JsonResponse(response_data, safe = False)

def addExpUserById(request, user_id):
	
	try:
		user = User.objects.filter(pk = user_id)
	except ObjectDoesNotExist:
		response_data = {}
		response_data['result'] = '404'
		response_data['message'] = 'Not Found: User not found'
		return JsonResponse(response_data, safe=False)

	else:

		if request.method == 'GET':
			data = serializers.serialize("json", user)
			return JsonResponse(json.loads(data), safe=False)

		if request.method == 'POST':
			form = UserFormUpdateExperience(request.POST)

			if form.is_valid():
				e = User.objects.get(pk = user_id)
				
				if form.cleaned_data['remove'] == "TRUE":
					e.experienceIn.remove(form.cleaned_data['exp_id'])

					expId = form.cleaned_data['exp_id']
					listEvents = Event.objects.filter(experience = expId)

					for singleEvent in listEvents:
						e.eventsIn.remove(singleEvent.pk)
					e.save()

					response_data = {}
					response_data['result'] = '200'
					response_data['message'] = 'OK: Successful'
					response_data['user'] = json.loads(serializers.serialize("json", [e,]))
					return JsonResponse(response_data, safe = False)
				else:
					e.experienceIn.add(form.cleaned_data['exp_id'])

					expId = form.cleaned_data['exp_id']
					listEvents = Event.objects.filter(experience = expId)

					for singleEvent in listEvents:
						e.eventsIn.add(singleEvent.pk)
					e.save()

					response_data = {}
					response_data['result'] = '200'
					response_data['message'] = 'OK: Successful'
					response_data['user'] = json.loads(serializers.serialize("json", [e,]))
					return JsonResponse(response_data, safe = False)
				
			else:
				response_data = {}
				response_data['result'] = '400'
				response_data['message'] = 'Bad Request'
				return JsonResponse(response_data, safe = False)

def addEventUserById(request, user_id):

	try:
		user = User.objects.filter(pk = user_id)
	except ObjectDoesNotExist:
		response_data = {}
		response_data['result'] = '404'
		response_data['message'] = 'Not Found: User not found'
		return JsonResponse(response_data, safe=False)

	else:

		if request.method == 'GET':

				data = serializers.serialize("json", user)
				return JsonResponse(json.loads(data), safe=False)

		if request.method == 'POST':

			form = UserFormUpdateEvent(request.POST)

			if form.is_valid():
				e = User.objects.get(pk = user_id)
				user = User.objects.filter(pk = user_id)

				if(form.cleaned_data['remove'] == "TRUE"):
					e.eventsIn.remove(form.cleaned_data['event_id'])
					e.save()

					response_data = {}
					response_data['result'] = '200'
					response_data['message'] = 'OK: Successful'
					response_data['user'] = json.loads(serializers.serialize("json", [e,]))
					return JsonResponse(response_data, safe = False)
				else:
					e.eventsIn.add(form.cleaned_data['event_id'])
					e.save()

					response_data = {}
					response_data['result'] = '200'
					response_data['message'] = 'OK: Successful'
					response_data['user'] = json.loads(serializers.serialize("json", [e,]))
					return JsonResponse(response_data, safe = False)

			else:
				response_data = {}
				response_data['result'] = '400'
				response_data['message'] = 'Bad Request'
				return JsonResponse(response_data, safe = False)


def addFriendUserById(request, user_id):

	try:
		user = User.objects.filter(pk = user_id)
	except ObjectDoesNotExist:
		response_data = {}
		response_data['result'] = '404'
		response_data['message'] = 'Not Found: User not found'
		return JsonResponse(response_data, safe=False)

	else:

		if request.method == 'GET':

				data = serializers.serialize("json", user)
				return JsonResponse(json.loads(data), safe=False)

		if request.method == 'POST':

			form = UserFormUpdateFriend(request.POST)

			if form.is_valid():
				e = User.objects.get(pk = user_id)
				if(form.cleaned_data['remove'] == "TRUE"):
					e.friends.remove(form.cleaned_data['user_id'])
					e.save()
					response_data = {}
					response_data['result'] = '200'
					response_data['message'] = 'OK: Successful'
					response_data['user'] = json.loads(serializers.serialize("json", [e,]))
					return JsonResponse(response_data, safe = False)
				else:
					e.friends.add(form.cleaned_data['user_id'])
					e.save()

					response_data = {}
					response_data['result'] = '200'
					response_data['message'] = 'OK: Successful'
					response_data['user'] = json.loads(serializers.serialize("json", [e,]))
					return JsonResponse(response_data, safe = False)

			else:
				response_data = {}
				response_data['result'] = '400'
				response_data['message'] = 'Bad Request'
				return JsonResponse(response_data, safe = False)

def removeUser(request):

	if request.method == 'POST':

		user_id = request.POST["user_id"]
	
		try:
			user = User.objects.filter(pk = user_id)	
		except ObjectDoesNotExist:
			response_data = {}
			response_data['result'] = '404'
			response_data['message'] = "Not Found: User not found"
			return JsonResponse(response_data, safe = False)

		else:
			user.delete()
			response_data = {}
			response_data['result'] = '200'
			response_data['message'] = 'OK: Successful'
			return JsonResponse(response_data, safe = False)