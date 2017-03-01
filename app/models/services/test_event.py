from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from services.models import Experience, User, Event

# class testCaseOne(TestCase):
#     def testThrees(self):
#         self.assertEqual(3,3)

# class EventTestCase(TestCase):

# 	def setUp(self):
# 		Event.objects.create()