from django.test import TestCase, Client, RequestFactory
from django.core.urlresolvers import reverse
from services.models import Experience, User, Event, Authenticator
from django.test import Client
from services.forms import UserFormCheckUser
from django.contrib.auth import hashers
import json

class TestAuth(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
            firstName='bob', lastName='builder', username = 'bobbuilds', password=hashers.make_password('cool_stuff'))
        self.user2 = User.objects.create(
            firstName='bill', lastName='billy', username = 'bbills', password=hashers.make_password('bumblebee'))
        self.user3 = User.objects.create(
            firstName='brad', lastName='red', username = 'plate', password=hashers.make_password('crazy'))
        self.auth1 = Authenticator.objects.create(user_id = 'darwin', authenticator = 'fklsjflsfkj')
        self.auth2 = Authenticator.objects.create(user_id = 'plato', authenticator = 'dfjsdjdjf')
        self.auth3 = Authenticator.objects.create(user_id = self.user3.pk, authenticator = 'dfjsdjdj')

    def testCreateAuthNew(self):
        form = {
            'user_id' : self.user2.username
        }
        resp = self.client.post('/api/v1/auth/create/', form).json()
        self.assertEqual(resp['result'], '200')

    def testCheckAuthValid(self):
        form = {
            'token' : self.auth1.authenticator
        }  
        resp = self.client.post('/api/v1/auth/check/', form).json()
        self.assertEqual(resp['result'], '200')

    def testCheckAuthInvalid(self):
        form = {
            'token' : 'dfkljfssdfs'
        }  
        resp = self.client.post('/api/v1/auth/check/', form).json()
        self.assertEqual(resp['result'], '404')

    def testCreateAuthReplace(self):
        form = {
            'user_id' : 'darwin'
        }
        resp = self.client.post('/api/v1/auth/create/', form).json()
        self.assertEqual(resp['result'], '200')

    def testRemoveAuth(self):
        form = {
            'token' : self.auth2.authenticator
        }
        resp = self.client.post('/api/v1/auth/remove/', form).json()
        self.assertEqual(resp['result'], '200')
        resp = self.client.post('/api/v1/auth/remove/', form).json()
        self.assertEqual(resp['result'], '404')

    def testCheckValidUser(self):
        form_data = {'username': self.user2.username, 'password': 'bumblebee'}
        resp = self.client.post('/api/v1/user/check/', form_data).json()
        self.assertEqual(resp['result'], '200')

    def testCheckInvalidUser(self):
        form_data = {'username': self.user2.username, 'password': 'notRight'}
        resp = self.client.post('/api/v1/user/check/', form_data).json()
        self.assertEqual(resp['result'], '404')

    def testUserByAuth(self):
        form = {
            'token' : self.auth3.authenticator
        }
        resp = self.client.post('/api/v1/user/auth/', form).json()
        self.assertEqual(resp['result'], '200')


    #tearDown method is called after each test
    def tearDown(self):
        pass #nothing to tear down