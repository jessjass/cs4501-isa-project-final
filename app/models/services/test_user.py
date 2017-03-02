from django.test import TestCase, Client, RequestFactory
from django.core.urlresolvers import reverse
from services.models import Experience, User, Event
from django.test import Client
from services.forms import UserFormUpdateExperience, UserFormUpdateEvent, UserFormUpdateFriend
import json

# class testCaseOne(TestCase):
#     def test_book(self):
#         self.assertEqual(1,2)

class TestUser(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
            firstName='bob', lastName='builder', username = 'bobbuilds', password='cool_stuff')
        self.user2 = User.objects.create(
            firstName='bill', lastName='billy', username = 'bbills', password='bumblebee')
        self.testExperience1 = Experience.objects.create(
            title="Exp 1", description="Not fun", totalPrice=19.99)
        self.testEvent1 = Event.objects.create(
            title="Go to the mall", description="Walk around and get food", price=10.00, datetime="2017-03-01T12:00:00Z")

    def testGetUserAll(self):
        resp = self.client.get('/api/v1/user/').json()
        
        self.assertEqual(resp[0]['fields']['username'], self.user1.username)
        self.assertEqual(resp[1]['fields']['username'], self.user2.username)

    def testGetUserById(self):
        resp = self.client.get('/api/v1/user/{0}/'.format(self.user1.pk)).json()

        self.assertEqual(resp[0]['fields']['username'], self.user1.username)

    def testPostUserById(self):
        form = {
            'firstName':'jessi',
            'lastName': 'jassal',
            'username': 'jessij',
            'password': 'jj'
        }
        resp = self.client.post('/api/v1/user/{0}/'.format(self.user1.pk), form).json()

        self.assertEqual(resp['result'], '200')
        self.assertEqual(resp['user'][0]['fields']['username'], form['username'])

    def testAddExpUserById(self):
        # form_data = {'exp_id': '0', 'remove': 'FALSE'}
        # form = UserFormUpdateExperience(data=form_data)
        # resp = self.client.post('/api/v1/user/experience/{0}/'.format(self.user1.pk), form).json()
        
        # self.assertEqual(resp['result'], '200')
        pass

    def testAddExpUserByIdRemove(self):
        # form_data = {'exp_id': '0', 'remove': 'TRUE'}
        # form = UserFormUpdateExperience(data=form_data)
        # resp = self.client.post('/api/v1/user/experience/{0}/'.format(self.user1.pk), form).json()
        
        # self.assertEqual(resp['result'], '200')
        pass

    def testAddEventUserById(self):
        # form_data = {'event_id': '0', 'remove': 'FALSE'}
        # form = UserFormUpdateEvent(data=form_data)
        # resp = self.client.post('/api/v1/user/event/{0}/'.format(self.user1.pk), form).json()
        
        # self.assertEqual(resp['result'], '200')
        pass    

    def testAddEventUserByIdRemove(self):
        # form_data = {'event_id': '0', 'remove': 'TRUE'}
        # form = UserFormUpdateEvent(data=form_data)
        # resp = self.client.post('/api/v1/user/event/{0}/'.format(self.user1.pk), form).json()
        
        # self.assertEqual(resp['result'], '200')
        pass   

    def testAddFriendUserById(self):
        # form_data = {'friend_id': '0', 'remove': 'FALSE'}
        # form = UserFormUpdateFriend(data=form_data)
        # resp = self.client.post('/api/v1/friend/event/{0}/'.format(self.user1.pk), form).json()
        
        # self.assertEqual(resp['result'], '200')
        pass

    def testAddFriendUserByIdRemove(self):
        # form_data = {'friend_id': '0', 'remove': 'TRUE'}
        # form = UserFormUpdateFriend(data=form_data)
        # resp = self.client.post('/api/v1/friend/event/{0}/'.format(self.user1.pk), form).json()
        
        # self.assertEqual(resp['result'], '200')
        pass    

    def testRemoveUser(self):
        form = {
            'user_id':self.user1.pk
        }

        resp = self.client.post('/api/v1/user/remove/', form).json()
        resp2 = self.client.post('/api/v1/user/remove/', form).json()
        
        self.assertEqual(resp['result'], '200')
        # self.assertEqual(resp2['result'], '404')

    #tearDown method is called after each test
    def tearDown(self):
        pass #nothing to tear down