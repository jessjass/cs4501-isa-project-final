from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from services.models import Experience, User, Event

import json

class TestEvent(TestCase):
	def setUp(self):
		self.testEvent = Event.objects.create(
			title="Eat tacos", description="Now", price=10.00, datetime="2017-03-01T12:00:00Z")
		pass

	def test_all_events(self):
		response = self.client.get('/api/v1/event/')
		response = json.loads(response.content.decode('utf-8'))

		print(str(response[0]['fields']['title']))
		self.assertEqual(response[0]['fields']['title'], self.testEvent.title)
		# self.assertTrue(response.context, '400')

	def tearDown(self):
		pass

