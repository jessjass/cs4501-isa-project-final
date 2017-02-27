from django.shortcuts import render

import urllib.request
import urllib.parse
from urllib.error import URLError
import json

exp_api = 'http://exp:8000'

def index(request):
	# Get resources from Experience API
	req = urllib.request.Request(exp_api + '/api/v1/')
	try:
		resp_json = urllib.request.urlopen(req)
	except URLError as e:
		experiences = {}
	else:
		resp_json = resp_json.read().decode('utf-8')
		resp = json.loads(resp_json)

	# Build context object
	context = {}
	context['experience_list'] = resp['experience']
	return render(request, 'index.html', context)

def experienceDetail(request, exp_id):
	context = {}
	return render(request, 'experience_detail.html', context)