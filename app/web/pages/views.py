from django.shortcuts import render

import urllib.request
import urllib.parse
from urllib.error import URLError
import json

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
		context['currentUser'] = resp['currentUser']

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

	return render(request, 'experience_detail.html', context)