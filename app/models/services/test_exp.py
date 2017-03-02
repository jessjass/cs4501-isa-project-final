from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from services.models import Experience, User, Event

class TestExperience(TestCase):
    
    def setUp(self):
        self.testExperience1 = Experience.objects.create(title="Exp 1", description="Not fun", totalPrice=19.99)
        self.testExperience2 = Experience.objects.create(title="Exp 2", description="A little fun", totalPrice=29.99)
        self.testExperience3 = Experience.objects.create(title="Exp 3", description="Pretty fun", totalPrice=39.99)
        self.testExperience4 = Experience.objects.create(title="Exp 4", description="Very fun", totalPrice=9.99)
        self.testExperience5 = Experience.objects.create(title="Exp 5", description="AMAZINGLY fun", totalPrice=119.99)

    def testGetAllExp(self):
        resp = self.client.get('/api/v1/experience/').json()
        
        self.assertEqual(resp['result'], '200')
        self.assertEqual(resp['experience'][0]['fields']['title'], self.testExperience1.title)
        self.assertEqual(resp['experience'][4]['fields']['title'], self.testExperience5.title)
    
    def testCreateNewExp(self):
        form = {
            'title':'New exp',
            'description':'New fun',
            'totalPrice':100.00
        }

        resp = self.client.post('/api/v1/experience/',form).json()

        self.assertEqual(resp['result'], '200')
        self.assertEqual(resp['experience'][0]['fields']['title'], form['title'])
    
    def testFailCreateNewExp(self):
        form = {
            'title':'New exp',
            'description':'New fun',
        }
        resp = self.client.post('/api/v1/experience/',form).json()
        self.assertEqual(resp['result'], '400')

    def testGetExpById(self):
        resp = self.client.get('/api/v1/experience/{0}/'.format(self.testExperience1.pk)).json()

        self.assertEqual(resp['result'], '200')
        self.assertEqual(resp['experience'][0]['fields']['title'], self.testExperience1.title)
    
    def testUpdateExpById(self):
        form = {
            'title':'Updated Exp',
            'description': 'Updated description',
            'totalPrice': 999.99
        }
        resp = self.client.post('/api/v1/experience/{0}/'.format(self.testExperience1.pk), form).json()

        self.assertEqual(resp['result'], '200')
        self.assertEqual(resp['experience'][0]['fields']['title'], form['title'])

    def testFailUpdateExpById(self):
        form = {
            'title':'Updated Exp',
            'description': 'Updated description',
            'price': 999.99
        }
        resp = self.client.post('/api/v1/experience/{0}/'.format(self.testExperience1.pk), form).json()

        self.assertEqual(resp['result'], '400')

    def testRemoveExperience(self):
        form = {
            'experience_id':self.testExperience1.pk
        }
        resp = self.client.post('/api/v1/experience/remove/', form).json()
        resp2 = self.client.post('/api/v1/experience/remove/', form).json()
        
        self.assertEqual(resp['result'], '200')
        self.assertEqual(resp2['result'], '404')
