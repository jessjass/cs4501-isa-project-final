from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json

from .models import Event, Experience, User
from .forms import EventForm, ExperienceForm, UserFormCreate, UserFormUpdateEvent, UserFormUpdateExperience

# "/" : entry point to Models API
def index(request):
	response_data = {}
	if request.method == 'GET':
		response_data['result'] = '200'
		response_data['message'] = "Successful: Entry point to the Models API."
		return JsonResponse(response_data, safe=False)

# "/events" : list of all events via GET or create an event via POST
def eventsAll(request):
	events = Event.objects.all()

	if request.method == 'GET':

		data = serializers.serialize("json", events)
		return JsonResponse(json.loads(data), safe=False)

	if request.method == 'POST':

		form = EventForm(request.POST)

		if form.is_valid():

			e = Event()
			e.title = form.cleaned_data['title']
			e.description = form.cleaned_data['description']
			e.datetime = form.cleaned_data['datetime']
			e.price = form.cleaned_data['price']
			e.save()

			response_data = {}
			response_data['result'] = '200'
			response_data['message'] = 'OK: Successful'
			response_data['event'] = json.loads(serializers.serialize("json", [e,]))
			return JsonResponse(response_data, safe = False)
		else:
			response_data = {}
			response_data['result'] = '400'
			response_data['message'] = 'Bad Request'
			return JsonResponse(response_data, safe = False)


# "/events/<event_id>/" : event by id via GET or event update via POST
def eventById(request, event_id):

	event = Event.objects.filter(pk = event_id)

	if not event:

		response_data = {}
		response_data['result'] = '404'
		response_data['message'] = 'Not Found: Event item not found'
		return JsonResponse(response_data, safe=False)

	else:

		if request.method == 'GET':

				data = serializers.serialize("json", event)
				return JsonResponse(json.loads(data), safe=False)

		if request.method == 'POST':

			form = EventForm(request.POST)

			if form.is_valid():
				e = Event.objects.get(pk = event_id)

				e.title = form.cleaned_data['title']
				e.description = form.cleaned_data['description']
				e.datetime = form.cleaned_data['datetime']
				e.price = form.cleaned_data['price']
				e.save()

				response_data = {}
				response_data['result'] = '200'
				response_data['message'] = 'OK: Successful'
				response_data['old'] = json.loads(serializers.serialize("json", event))
				response_data['event'] = json.loads(serializers.serialize("json", [e,]))
				return JsonResponse(response_data, safe = False)
			else:
				response_data = {}
				response_data['result'] = '400'
				response_data['message'] = 'Bad Request'
				return JsonResponse(response_data, safe = False)


def eventByExpId(request, exp_id):
	event = Event.objects.filter(experience = exp_id)

	if not event:
		response_data = {}
		response_data['result'] = '404'
		response_data['message'] = 'Not Found: Event item not found'
		return JsonResponse(response_data, safe=False)

	else:
		if request.method == 'GET':
			data = serializers.serialize("json", event)
			return JsonResponse(json.loads(data), safe=False)

# "/events/remove/" : event removal by event_id (or ALL) via POST 
def remove(request):

	if request.method == 'POST':

		event_id = request.POST["event_id"]
		if event_id == "ALL":
			Event.objects.all().delete()
			response_data = {}
			response_data['result'] = '200'
			response_data['message'] = 'OK: Successful'
			return JsonResponse(response_data, safe = False)

		else:
			event = Event.objects.filter(pk = event_id)	

			if not event:
				response_data = {}
				response_data['result'] = '404'
				response_data['message'] = "Not Found: Event item not found"
				return JsonResponse(response_data, safe = False)

			else:
				event.delete()
				response_data = {}
				response_data['result'] = '200'
				response_data['message'] = 'OK: Successful'
				return JsonResponse(response_data, safe = False)

# "/experience" : list of all experiences via GET or create an event via POST
def experienceAll(request):
	experiences = Experience.objects.all()

	if request.method == 'GET':

		data = serializers.serialize("json", experiences)
		return JsonResponse(json.loads(data), safe=False)

	if request.method == 'POST':

		form = ExperienceForm(request.POST)

		if form.is_valid():

			e = Experience()
			e.title = form.cleaned_data['title']
			e.description = form.cleaned_data['description']
			e.totalPrice = form.cleaned_data['totalPrice']
			e.save()

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
def experienceById(request, experience_id):

	experience = Experience.objects.filter(pk = experience_id)

	if not experience:

		response_data = {}
		response_data['result'] = '404'
		response_data['message'] = 'Not Found: Experience item not found'
		return JsonResponse(response_data, safe=False)

	else:

		if request.method == 'GET':

				data = serializers.serialize("json", experience)
				return JsonResponse(json.loads(data), safe=False)

		if request.method == 'POST':

			form = ExperienceForm(request.POST)

			if form.is_valid():
				e = Experience.objects.get(pk = experience_id)

				e.title = form.cleaned_data['title']
				e.description = form.cleaned_data['description']
				e.totalPrice = form.cleaned_data['totalPrice']
				e.save()

				response_data = {}
				response_data['result'] = '200'
				response_data['message'] = 'OK: Successful'
				response_data['old'] = json.loads(serializers.serialize("json", experience))
				response_data['experience'] = json.loads(serializers.serialize("json", [e,]))
				return JsonResponse(response_data, safe = False)
			else:
				response_data = {}
				response_data['result'] = '400'
				response_data['message'] = 'Bad Request'
				return JsonResponse(response_data, safe = False)


# "/experience/remove/" : experience removal by experience_id (or ALL) via POST 
def removeExperience(request):

	if request.method == 'POST':

		experience_id = request.POST['experience_id']
	
		experience = Experience.objects.filter(pk = experience_id)	

		if not experience:
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
	user = User.objects.all()

	if request.method == 'GET':

		data = serializers.serialize("json", user)
		return JsonResponse(json.loads(data), safe=False)

	if request.method == 'POST':

		form = UserFormCreate(request.POST)

		if form.is_valid():

			e = User()
			e.firstName = form.cleaned_data['firstName']
			e.lastName = form.cleaned_data['lastName']
			e.username = form.cleaned_data['username']
			e.password = form.cleaned_data['password'] 
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

def userById(request, user_id):

	user = User.objects.filter(pk = user_id)

	if not user:

		response_data = {}
		response_data['result'] = '404'
		response_data['message'] = 'Not Found: user not found'
		return JsonResponse(response_data, safe=False)

	else:

		if request.method == 'GET':

				data = serializers.serialize("json", user)
				return JsonResponse(json.loads(data), safe=False)

		if request.method == 'POST':

			form = UserFormUpdateEvent(request.POST)

			if form.is_valid():
				e = User.objects.get(pk = user_id)

				e.firstName = form.cleaned_data['firstName']
				e.lastName = form.cleaned_data['lastName']
				e.username = form.cleaned_data['username']
				e.password = form.cleaned_data['password'] 
				e.eventsIn.add(form.cleaned_data['event_id'])
				e.save()

				response_data = {}
				response_data['result'] = '200'
				response_data['message'] = 'OK: Successful'
				response_data['old'] = json.loads(serializers.serialize("json", user))
				response_data['user'] = json.loads(serializers.serialize("json", [e,]))
				return JsonResponse(response_data, safe = False)

			else:
				response_data = {}
				response_data['result'] = '400'
				response_data['message'] = 'Bad Request'
				return JsonResponse(response_data, safe = False)

def addExpUserById(request, user_id):
	user = User.objects.filter(pk = user_id)

	if not user:

		response_data = {}
		response_data['result'] = '404'
		response_data['message'] = 'Not Found: user not found'
		return JsonResponse(response_data, safe=False)

	else:

		if request.method == 'GET':

				data = serializers.serialize("json", user)
				return JsonResponse(json.loads(data), safe=False)

		if request.method == 'POST':

			form = UserFormUpdateExperience(request.POST)

			if form.is_valid():
				e = User.objects.get(pk = user_id)
				e.experienceIn.add(form.cleaned_data['exp_id'])

				expId = form.cleaned_data['exp_id']
				listEvents = Event.objects.filter(experience = expId)

				for singleEvent in listEvents:
					e.eventsIn.add(singleEvent.pk)
				e.save()

				response_data = {}
				response_data['result'] = '200'
				response_data['message'] = 'OK: Successful'
				response_data['old'] = json.loads(serializers.serialize("json", user))
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
	
		user = User.objects.filter(pk = user_id)	

		if not user:
			response_data = {}
			response_data['result'] = '404'
			response_data['message'] = "Not Found: user item not found"
			return JsonResponse(response_data, safe = False)

		else:
			user.delete()
			response_data = {}
			response_data['result'] = '200'
			response_data['message'] = 'OK: Successful'
			return JsonResponse(response_data, safe = False)