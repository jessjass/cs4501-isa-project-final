from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from services.models import Experience, User, Event

import json

class TestEvent(TestCase):

	def setUp(self):
		self.testEvent = Event.objects.create(
			title="Go to the mall", description="Walk around and get food", price=10.00, datetime="2017-03-01T12:00:00Z")
		pass

	def testAll(self):
		resp = self.client.get('/api/v1/event/')
		json_resp = json.loads(resp.content.decode('utf-8'))

		print(json_resp['result'])
		print(json_resp)

		self.assertEqual(resp.status_code, 200)
		self.assertEqual(json_resp[0]['fields']['title'], self.testEvent.title)

	def testGetEventById(self):
		resp = self.client.get('/api/v1/event/{0}/'.format(self.testEvent.pk))
		json_resp = json.loads(resp.content.decode('utf-8'))

		print(resp)
		print(json_resp)

		self.assertEqual(resp.status_code, 200)
		self.assertEqual(json_resp[0]['fields']['title'], self.testEvent.title)

	# def testAddEvent(self):
	# 	form = {
	# 		'title' : 'Watching a movie',
	# 		'description' : 'Logan, 8pm, Regal Stonefield',
	# 		'price' : '12.50',
	# 		'datetime' : '2017-03-01T12:00:00Z'
	# 	}

	# 	resp = self.client.post('/api/v1/event/', form)
	# 	json_resp = json.loads(resp.content.decode('utf-8'))

	# 	self.assertEqual(resp.status_code, 200)

	# 	print(json_resp)


	def tearDown(self):
		pass

