from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import hashers
from django.core.urlresolvers import reverse, resolve

import urllib.request
import urllib.parse
from urllib.error import URLError
import json
import requests

from .forms import CreateEventForm, SignInForm, SignUpForm

exp_api = 'http://exp:8000'

def login_required(f):
    def wrap(request, *args, **kwargs):
        # try authenticating the user
        user = validate(request)
		
        # authentication failed
        if not user:
            # redirect the user to the login page
            return redirect('signIn')
        else:
            kwargs['user'] = user
            return f(request, *args, **kwargs)
    return wrap

def anonymous_user(f):
	def wrap(request, *args, **kwargs):
		user = validate(request)

		if user:
			return redirect('home')
		else:
			return f(request, *args, **kwargs)
	return wrap

def validate(request):
	if 'auth' in request.COOKIES:
		auth = request.COOKIES['auth']
		post_data = {}
		post_data['auth'] = auth
		try:
			resp = requests.post(exp_api + "/api/v1/checkUser/" , post_data)
		except requests.exceptions.RequestException as e:
			return HttpResponse(e)
		else:
			if resp.json()['result'] == "200":
				return resp.json()['user']
			else: 
				return False
	else:
		return False

def index(request):
	context = {}
	# req = urllib.request.Request(exp_api + '/api/v1/')
	
	try:
		if 'auth' in request.COOKIES:
			authCookie = request.COOKIES['auth']
			cookie = dict(auth=authCookie)
			resp_json = requests.get(exp_api + '/api/v1/', cookies=cookie)
		else:
			resp_json = requests.get(exp_api + '/api/v1/')
	except URLError as e:
		context['experience_list'] = []
	else:
		# resp_json = resp_json.read().decode('utf-8')
		# resp = json.loads(resp_json)
		resp = resp_json.json()
		context['experience_list'] = resp['experience']
		if(resp['currentUser']['result'] == '200'):
			currentUser = resp['currentUser']['user'][0]['fields']
			userData = {}
			userData['firstName'] = currentUser['firstName']
			userData['lastName'] = currentUser['lastName']
			context['auth'] = userData

	return render(request, 'index.html', context)

@login_required
def experienceDetail(request, exp_id, **kwargs):
	context = {}
	# req = urllib.request.Request(exp_api + '/api/v1/experience/' + exp_id + '/')
	
	try:
		# resp_json = urllib.request.urlopen(req)
		if 'auth' in request.COOKIES:
			authCookie = request.COOKIES['auth']
			cookie = dict(auth=authCookie)
			resp_json = requests.get(exp_api + '/api/v1/experience/' + exp_id +'/', cookies=cookie)
		else:
			resp_json = requests.get(exp_api + '/api/v1/experience/' + exp_id + '/')
	except URLError as e:
		context['experience_events'] = []
	else:
		# resp_json = resp_json.read().decode('utf-8')
		# resp = json.loads(resp_json)
		resp = resp_json.json()
		context['experience_events'] = resp['experience_events']
		if(resp['currentUser']['result'] == '200'):
			currentUser = resp['currentUser']['user'][0]['fields']
			userData = {}
			userData['firstName'] = currentUser['firstName']
			userData['lastName'] = currentUser['lastName']
			context['auth'] = userData

	if context['experience_events'] == []:
		context['exp_id'] = exp_id
		return render(request, 'experience_detail_error.html', context)
	else:
		return render(request, 'experience_detail.html', context)

@anonymous_user
def signUp(request):
	context = {}
	if request.method == 'GET':

		form = SignUpForm()
		context['form'] = form
		return render(request, 'sign_up.html', context)

	if request.method == 'POST':
		form = SignUpForm(request.POST)

		if not form.is_valid():
			context['form'] = form
			return render(request, 'sign_up.html', context)

		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		confirm_password = form.cleaned_data['confirm_password']
		firstName = form.cleaned_data['firstName']
		lastName = form.cleaned_data['lastName']

		if password != confirm_password:
			context['form'] = form
			context['passwordError'] = "Passwords do not match"
			return render(request, 'sign_up.html', context)

		post_data = {
			'username' : username,
			'password' : hashers.make_password(password),
			'firstName' : firstName,
			'lastName' : lastName
		}

		try:
			resp = requests.post(exp_api + '/api/v1/signup/', post_data)
		except requests.exceptions.RequestException as e:
			return HttpResponse(e)
		else:
			resp_data = resp.json()
			context['firstName'] = resp_data['user'][0]['fields']['firstName']
			return render(request, 'sign_up_success.html', context)

def signOut(request):
	context = {}
	if request.method == 'GET':
		auth = request.COOKIES['auth']
		post_data = {}
		post_data['auth'] = auth
		try:
			resp = requests.post(exp_api + "/api/v1/signout/", post_data)
		except requests.exceptions.RequestException as e:
			return HttpResponse(e)
		else:
			if resp.json()['result'] == "200":
				return redirect('home')
			else: 
				return redirect('home')
				
@anonymous_user
def signIn(request):
	context = {}
	if request.method == 'GET':
		form = SignInForm()
		context['form'] = form
		return render(request, 'sign_in.html', context)

	if request.method == 'POST':
		form = SignInForm(request.POST)

		if not form.is_valid():
			context['form'] = form
			context['error'] = "true"
			return render(request,'sign_in.html', context)

		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		
		post_data = {
			'username' : username,
			'password' : password
		}

		try:
			resp = requests.post(exp_api + "/api/v1/signin/" , post_data)
		except requests.exceptions.RequestException as e:
			return HttpResponse(e)
		else:
			if not resp or resp.json()['result'] != '200':
				context["error"] = "true"
				context['form'] = form
				return render(request,'sign_in.html', context)
			else:
				authenticator = resp.json()['auth']
				# newURL = reverse('home')
				# response = HttpResponseRedirect(newURL)
				response = redirect('home')
				response.set_cookie("auth", authenticator)
				return response

@login_required
def createEvent(request):
	context = {}
	if request.method == 'POST':
		form = CreateEventForm(request.POST)

		if not form.is_valid():
			context['form'] = form
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