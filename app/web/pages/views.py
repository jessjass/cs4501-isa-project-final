from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

import urllib.request
import urllib.parse
from urllib.error import URLError
import json
import requests

from .forms import CreateEventForm, SignInForm

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

def signIn(request):
	context = {}
	if request.method == 'GET':
		form = SignInForm()
		context['form'] = form
		return render(request, 'sign_in.html', context)

	if request.method == 'POST':
		form = SignInForm(request.POST)

		if not form.is_valid():
			return render(request,'sign_in.html', context)

		username = form.cleaned_data['username']
		password = form.cleaned_data['password']

		# Not working... not sure why...
		# next = form.cleaned_data.get('next') or reverse('home')
		
		post_data = {
			'username' : username,
			'password' : password
		}

		return JsonResponse(post_data)

		# NEED TO FINISH EXPERIENCE LAYER TO FINISH REST

		# try:
		# 	resp = requests.post(exp_api + , post_data)
		# except requests.exceptions.RequestException as e:
		# 	return HttpResponse(e)
		# else:
		# 	return render()

		# if not resp or not resp['ok']:
		# 	return render(request,'sign_in.html', context)

		# # ToDo: update resp_json indices
		# authenticator = resp['resp']['authenticator']

		# response = HttpResponseRedirect(next)
		# response.set_cookie("auth", authenticator)

		# return response

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
			return render(request, 'create_event_success.html', context)

	if request.method == 'GET':
		form = CreateEventForm()
		context['form'] = form
		context['title'] = 'col-md-12'
		context['description'] = 'col-md-12'
		context['date'] = 'col-md-4'
		context['time'] = 'col-md-4'
		context['price'] = 'col-md-4'

		return render(request, 'create_event.html', context)