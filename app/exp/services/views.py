from django.http import HttpResponse, JsonResponse, FileResponse
from django.core import serializers
from elasticsearch import Elasticsearch
from kafka import KafkaProducer

import urllib.request
import urllib.parse
from urllib.error import URLError
import json
import requests

models_api = 'http://models:8000'


# "/" : resources for home page (index.html)
def index(request):
    response_data = {}
    post_data = {}

    if request.method == 'GET':
        # Get experiences from Models API
        if 'auth' in request.COOKIES:
            auth = request.COOKIES['auth']
            post_data['token'] = auth

        req = urllib.request.Request(models_api + '/api/v1/experience/')
        # userReq = urllib.request.Request(models_api + '/api/v1/user/1')

        try:
            resp_json = urllib.request.urlopen(req)
            # userResp_json = urllib.request.urlopen(userReq)
            userInfo = requests.post(models_api + '/api/v1/user/auth/', post_data)

        except URLError as e:
            # URLError
            if hasattr(e, 'reason'):
                response_data['result'] = "400"
                response_data['message'] = 'We failed to reach a server. Reason: ' + e.reason
            # HTTPError
            elif hasattr(e, 'code'):
                response_data['result'] = e.code  # error code
                response_data['message'] = 'The server couldn\'t fulfill the request.'
        else:
            resp_json = resp_json.read().decode('utf-8')
            # userResp_json = userResp_json.read().decode('utf-8')

            resp = json.loads(resp_json)
            # userResp = json.loads(userResp_json)
            currentUser = userInfo.json()

            response_data['result'] = "200"
            response_data['message'] = "OK: Successful"
            response_data['experience'] = resp['experience']
            response_data['currentUser'] = currentUser

        return JsonResponse(response_data, safe=False)


def experienceDetail(request, exp_id):
    response_data = {}
    post_data = {}

    if request.method == 'GET':
        if 'auth' in request.COOKIES:
            auth = request.COOKIES['auth']
            post_data['token'] = auth

        req = urllib.request.Request(models_api + '/api/v1/event/experience/' + exp_id + '/')
        # userReq = urllib.request.Request(models_api + '/api/v1/user/1')

        try:
            resp_json = urllib.request.urlopen(req)
            # userResp_json = urllib.request.urlopen(userReq)
            userInfo = requests.post(models_api + '/api/v1/user/auth/', post_data)

        except URLError as e:
            # URLError
            if hasattr(e, 'reason'):
                response_data['result'] = "400"
                response_data['message'] = 'We failed to reach a server. Reason: ' + e.reason
            # HTTPError
            elif hasattr(e, 'code'):
                response_data['result'] = e.code  # error code
                response_data['message'] = 'The server couldn\'t fulfill the request.'
        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": e}, safe=False)

        else:
            resp_json = resp_json.read().decode('utf-8')
            # userResp_json = userResp_json.read().decode('utf-8')

            resp = json.loads(resp_json)
            # userResp = json.loads(userResp_json)
            currentUser = userInfo.json()

            response_data['result'] = "200"
            response_data['message'] = "OK: Successful"
            response_data['experience_events'] = resp['event_list']
            response_data['currentUser'] = currentUser

        return JsonResponse(response_data, safe=False)


def signUp(request):
    response_data = {}
    post_data = {}

    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']
        password = request.POST['password']

        post_data['firstName'] = firstName
        post_data['lastName'] = lastName
        post_data['username'] = username
        post_data['password'] = password

        try:
            resp = requests.post(models_api + '/api/v1/user/', post_data)
        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": e}, safe=False)
        else:
            return JsonResponse(resp.json())


def signOut(request):
    response_data = {}
    post_data = {}

    if request.method == 'POST':
        post_data['token'] = request.POST['auth']

        try:
            resp = requests.post(models_api + '/api/v1/auth/remove/', post_data)
        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": e}, safe=False)
        else:
            return JsonResponse(resp.json())


def signIn(request):
    response_data = {}
    post_data = {}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        post_data['username'] = username
        post_data['password'] = password

        try:
            resp = requests.post(models_api + '/api/v1/user/check/', post_data)
        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": e}, safe=False)
        else:
            response = resp.json()
            if response['result'] == '200':
                try:
                    auth_data = {}
                    auth_data['user_id'] = response['user_id']
                    authresp = requests.post(models_api + '/api/v1/auth/create/', auth_data)
                except requests.exceptions.RequestException as e:
                    return JsonResponse({"error": e}, safe=False)
                else:
                    response['auth'] = authresp.json()['auth'][0]['pk']
                    return JsonResponse(response)
            else:
                return JsonResponse(response)


def checkUserAuth(request):
    if request.method == 'POST':
        auth_data = {}
        auth_data['token'] = request.POST['auth']
        try:
            authresp = requests.post(models_api + '/api/v1/auth/check/', auth_data)
            userInfo = requests.post(models_api + '/api/v1/user/auth/', auth_data)

        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": e}, safe=False)
        else:
            if (authresp.json()['result'] == '200'):
                response_data = {}
                response_data['result'] = "200"
                response_data['message'] = "OK: User authenticated"
                response_data['user'] = userInfo.json()
                return JsonResponse(response_data)
            else:
                response_data = {}
                response_data['result'] = "404"
                response_data['message'] = "Error: Unknown User"
                return JsonResponse(response_data)


def getEventImage(request, event_id):
    if request.method == 'GET':
        try:
            resp = requests.get(models_api + '/api/v1/event/image/' + event_id + '/')
        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": e}, safe=False)
        else:
            return FileResponse(resp)


def userDashboard(request, user_id):
    response_data = {}

    if request.method == 'GET':
        try:
            resp = requests.get(models_api + '/api/v1/event?createdBy=' + user_id)
        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": e}, safe=False)
        else:
            response_data['event_list'] = resp.json()
            return JsonResponse(response_data['event_list'])


def createEvent(request):
    response_data = {}
    post_data = {}
    file_data = {}

    if request.method == 'POST':
        title = request.POST['title']
        date = request.POST['date']
        time = request.POST['time']
        price = request.POST['price']
        description = request.POST['description']
        createdBy = request.POST['createdBy']
        image = request.FILES['image']

        post_data['title'] = title
        post_data['datetime'] = date + ' ' + time
        post_data['price'] = price
        post_data['description'] = description
        post_data['createdBy'] = createdBy
        file_data['image'] = image

        try:
            resp = requests.post(models_api + '/api/v1/event/', data=post_data, files=file_data)
        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": e}, safe=False)
        else:
            itemId = resp.json()['event'][0]['pk']

            response_data['result'] = "200"
            response_data['message'] = "OK: Successful"

            producer = KafkaProducer(bootstrap_servers='kafka:9092')
            new_listing = {
                'title': title,
                'description': description,
                'id': itemId,
                'date': date,
                'time': time,
                'price': price
            }
            producer.send('new-listings-topic', json.dumps(new_listing).encode('utf-8'))
            return JsonResponse(response_data, safe=False)


def searchEvent(request):
    response_data = {}

    if request.method == 'GET':
        query = request.GET['search']
        try:
            es = Elasticsearch(['es'])
            data = es.search(index='listing_index', body={'query': {'query_string': {'query': query}}, 'size': 10})
        except:
            response_data['result'] = "400"
            response_data['message'] = "Failed to search"
            return JsonResponse(response_data, safe=False)
        else:
            response_data['result'] = "200"
            response_data['message'] = "OK: Successful"
            response_data['data'] = data
            return JsonResponse(response_data, safe=False)


