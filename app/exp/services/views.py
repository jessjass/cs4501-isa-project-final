from django.http import HttpResponse, JsonResponse
from django.core import serializers

import urllib.request
import urllib.parse
from urllib.error import URLError
import json

models_api = 'http://models:8000'

# "/" : resources for home page (index.html)
def index(request):
	response_data = {}

	if request.method == 'GET':
		
		# Get experiences from Models API
		req = urllib.request.Request(models_api + '/api/v1/experience/')
		userReq = urllib.request.Request(models_api + '/api/v1/user/1')
		try:
			resp_json = urllib.request.urlopen(req)
			userResp_json = urllib.request.urlopen(userReq)
		except URLError as e:
			# URLError
			if hasattr(e, 'reason'):
				response_data['result'] = "400"
				response_data['message'] = 'We failed to reach a server. Reason: ' + e.reason
			# HTTPError
			elif hasattr(e, 'code'):
				response_data['result'] = e.code # error code
				response_data['message'] = 'The server couldn\'t fulfill the request.'
		else:
			resp_json = resp_json.read().decode('utf-8')
			userResp_json = userResp_json.read().decode('utf-8')

			resp = json.loads(resp_json)
			userResp = json.loads(userResp_json)

			response_data['result'] = "200"
			response_data['message'] = "OK: Successful"
			response_data['experience'] = resp
			response_data['currentUser'] = userResp
		
		return JsonResponse(response_data, safe=False)

def experienceDetail(request, exp_id):
	response_data = {}

	if request.method == 'GET':
		req = urllib.request.Request(models_api + '/api/v1/event/experience/' + exp_id + '/')
		userReq = urllib.request.Request(models_api + '/api/v1/user/1')

		try:
			resp_json = urllib.request.urlopen(req)
			userResp_json = urllib.request.urlopen(userReq)

		except URLError as e:
			# URLError
			if hasattr(e, 'reason'):
				response_data['result'] = "400"
				response_data['message'] = 'We failed to reach a server. Reason: ' + e.reason
			# HTTPError
			elif hasattr(e, 'code'):
				response_data['result'] = e.code # error code
				response_data['message'] = 'The server couldn\'t fulfill the request.'
		else:
			resp_json = resp_json.read().decode('utf-8')
			userResp_json = userResp_json.read().decode('utf-8')

			resp = json.loads(resp_json)
			userResp = json.loads(userResp_json)

			response_data['result'] = "200"
			response_data['message'] = "OK: Successful"
			response_data['experience_events'] = resp
			response_data['currentUser'] = userResp

		return JsonResponse(response_data, safe=False)



