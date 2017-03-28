from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from services.models import Experience, User, Event

import json

class TestEvent(TestCase):

	def setUp(self):
		self.testExperience = Experience.objects.create(
			title="Fun day", description="Lots of fun", totalPrice=19.99)
		self.testEvent = Event.objects.create(
			title="Go to the mall", description="Walk around and get food", price=10.00, datetime="2017-03-01T12:00:00Z")
		self.testEvent2 = Event.objects.create(
			title="Eat tacos", description="We eat tacos", price=9.99, datetime="2017-03-01T12:00:00Z", experience=self.testExperience)
		self.testEvent3 = Event.objects.create(
			title="Got to concert", description="Kendrick Lamar", price=79.99, datetime="2017-03-01T12:00:00Z", experience=self.testExperience)
		pass

	def testGetAllEvents(self):
		''' Test for getting all events '''
		resp = self.client.get('/api/v1/event/').json()

		self.assertEqual(resp['result'], '200')
		self.assertEqual(resp['event_list'][0]['fields']['title'], self.testEvent.title)

	def testGetEventById(self):
		''' Test for getting event by id '''
		resp = self.client.get('/api/v1/event/{0}/'.format(self.testEvent.pk)).json()

		self.assertEqual(resp['result'], '200')
		self.assertEqual(resp['event'][0]['fields']['title'], self.testEvent.title)

	def testGetEventByIdDNE(self):
		''' Test for getting event by id where id doesn't exist '''
		resp = self.client.get('/api/v1/event/100/').json()

		self.assertEqual(resp['result'], '404')
		self.assertEqual(resp['message'], 'Not Found: Event item not found')

	# def testAddEvent(self):
	# 	''' Test for creating an event '''
	# 	form = {
	# 		'title' : 'Watching a movie',
	# 		'description' : 'Logan 8pm Regal Stonefield',
	# 		'price' : 12.50,
	# 		'datetime' : '2017-03-01 12:00:00'
	# 	}

	# 	resp = self.client.post('/api/v1/event/', form).json()

	# 	self.assertEqual(resp['result'], '200')
	# 	self.assertEqual(resp['event'][0]['fields']['title'], form['title'])

	def testGetEventByExperience(self):
		''' Test for getting all events in an experience '''
		resp = self.client.get('/api/v1/event/experience/{0}/'.format(self.testExperience.pk)).json()

		self.assertEqual(resp['result'], '200')

		event_titles = []
		for event in resp['event_list']:
			event_titles.append(event['fields']['title'])

		self.assertIn(self.testEvent2.title, event_titles)
		self.assertIn(self.testEvent3.title, event_titles)

	def testRemoveEvent(self):
		''' Test for removing an event '''
		form = {
			'event_id' : self.testEvent.pk
		}
		resp = self.client.post('/api/v1/event/remove/', form).json()
		
		self.assertEqual(resp['result'], '200')
		self.assertEqual(resp['message'], 'OK: Successful')

	def testRemoveEventDNE(self):
		''' Test for removing an event that doesn't exist '''
		form = {
			'event_id' : 100
		}
		resp = self.client.post('/api/v1/event/remove/', form).json()
		
		self.assertEqual(resp['result'], '404')
		self.assertEqual(resp['message'], 'Not Found: Event item not found')

	def tearDown(self):
		pass

