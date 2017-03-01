from django.test import TestCase, Client, RequestFactory
from django.core.urlresolvers import reverse
from services.models import Experience, User, Event
from django.test import Client
import json

# class testCaseOne(TestCase):
#     def test_book(self):
#         self.assertEqual(1,2)

class getUserDetailsTestCase(TestCase):
    def setUp(self):
        #self.factory = RequestFactory()
        #self.c = Client()
        self.user = User.objects.create(
            firstName='bob', lastName='builder', username = 'bobbuilds', password='cool_stuff') 

    def testsuccess(self):
        # Create an instance of a GET request.

        # request = self.factory.get('/v1/user/1/')

        response = self.client.get(reverse('getById', kwargs={'user_id':1}))

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.

        # request.user = self.user
        dc = json.loads(response.content.decode("utf-8"))[0]['fields']
        print (dc['firstName'])
        self.assertEquals(response.status_code, 200)

    #tearDown method is called after each test
    def tearDown(self):
        pass #nothing to tear down