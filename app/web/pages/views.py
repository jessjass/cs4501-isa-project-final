from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


import urllib.request
import urllib.parse
from urllib.error import URLError
import json
import requests

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
	context = {}
	return render(request, 'sign_in.html', context)

def createEvent(request):
	context = {}

	if request.method == 'POST':

		post_data = {
			'inputEventTitle' : request.POST['inputEventTitle'],
			'inputEventDescription' : request.POST['inputEventDescription'],
			'inputEventDate' : request.POST['inputEventDate'],
			'inputEventTime' : request.POST['inputEventTime'],
			'inputEventPrice' : request.POST['inputEventPrice']
		}

		try:
			resp = requests.post(exp_api + '/api/v1/event/create/', post_data)
		except requests.exceptions.RequestException as e:
			return HttpResponse(e)
		else:
			return JsonResponse(resp.json())

	if request.method == 'GET':
		return render(request, 'create_event.html', context)

def signIn(request):
	if request.method == 'POST':
		# Send validated information to our experience layer
		email = request.POST.get("inputEmail")
		password = request.POST.get("inputPassword")
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