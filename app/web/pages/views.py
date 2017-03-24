from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import urllib.request
import urllib.parse
from urllib.error import URLError
import json
import requests

from .forms import CreateEventForm

exp_api = 'http://exp:8000'

def index(request):
	context = {}
	req = urllib.request.Request(exp_api + '/api/v1/')
	
	try:
		resp_json = urllib.request.urlopen(req)
	except URLError as e:
		context['experience_list'] = []
	else:
		resp_json = resp_json.read().decode('utf-8')
		resp = json.loads(resp_json)
		context['experience_list'] = resp['experience']
		# context['currentUser'] = resp['currentUser']

	return render(request, 'index.html', context)

def experienceDetail(request, exp_id):
	context = {}
	req = urllib.request.Request(exp_api + '/api/v1/experience/' + exp_id + '/')
	
	try:
		resp_json = urllib.request.urlopen(req)
	except URLError as e:
		context['experience_events'] = []
	else:
		resp_json = resp_json.read().decode('utf-8')
		resp = json.loads(resp_json)
		context['experience_events'] = resp['experience_events']
		context['currentUser'] = resp['currentUser']
	
	if context['experience_events'] == []:
		context['exp_id'] = exp_id
		return render(request, 'experience_detail_error.html', context)
	else:
		return render(request, 'experience_detail.html', context)

def signInPage(request):
	return render(request, 'sign_in.html')

def createEvent(request):
	context = {}
	if request.method == 'POST':

		form = CreateEventForm(request.POST)

		if not form.is_valid():
			return render(request, 'create_event.html', context)

		post_data = {
			'title' : form.cleaned_data['title'],
			'description' : form.cleaned_data['description'],
			'date' : form.cleaned_data['date'],
			'time' : form.cleaned_data['time'],
			'price' : form.cleaned_data['price']
		}

		try:
			resp = requests.post(exp_api + '/api/v1/event/create/', post_data)
		except requests.exceptions.RequestException as e:
			return HttpResponse(e)
		else:
			return JsonResponse(resp.json())

	if request.method == 'GET':
		form = CreateEventForm()
		context['form'] = form
		context['title'] = 'col-md-12'
		context['description'] = 'col-md-12'
		context['date'] = 'col-md-4'
		context['time'] = 'col-md-4'
		context['price'] = 'col-md-4'

		return render(request, 'create_event.html', context)

def signIn(request):
	if request.method == 'POST':
		# Send validated information to our experience layer
		email = request.POST.get("inputEmail")
		password = request.POST.get("inputPassword")

		post_data = {
			'inputEmail' : request.POST['inputEmail'],
			'inputPassword' : request.POST['inputPassword']
		}

		resp = urllib.request.Request(exp_api + '/api/v1/experience/signin/')

		try:
			resp_json = urllib.request.urlopen(req)
		except URLError as e:
			# ToDo: Add response redirects to 'login error' page

			# URLError
			if hasattr(e, 'reason'):
				response_data['result'] = "400"
				response_data['message'] = 'We failed to reach a server. Reason: ' + e.reason
			# HTTPError
			elif hasattr(e, 'code'):
				response_data['result'] = e.code # error code
				response_data['message'] = 'The server couldn\'t fulfill the request.'
		else:

			""" If we made it here, we can log them in. """
			# Set their login cookie and redirect to back to wherever they came from
			
			# ToDo: update resp_json indices
			authenticator = resp_json['resp']['authenticator']

			# response to return to home
			response = HttpResponseRedirect(exp_api + '/api/v1/')
			response.set_cookie("auth", authenticator, max_age=3600)

	# return to index page
	return response