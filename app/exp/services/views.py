from django.http import HttpResponse, JsonResponse
from django.core import serializers

import urllib.request
import urllib.parse
import json

models_api = 'http://models:8000'

# "/" : entry point to Experience API
def index(request):
	response_data = {}
	if request.method == 'GET':
		req = urllib.request.Request(models_api + '/api/v1/experience/')
		resp_json = urllib.request.urlopen(req).read().decode('utf-8')
		resp = json.loads(resp_json)

		response_data['result'] = "200"
		response_data['message'] = "Successful: Entry point to the Experience API."
		# return JsonResponse(response_data, safe=False)
		return JsonResponse(resp, safe=False)