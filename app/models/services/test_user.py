from django.test import TestCase, Client, RequestFactory
from django.core.urlresolvers import reverse
from services.models import Experience, User, Event

# class testCaseOne(TestCase):
#     def test_book(self):
#         self.assertEqual(1,2)

# class getUserDetailsTestCase(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(
#             firstName='bob', lastName='builder', username = 'bobbuilds', password='cool_stuff') 

#     def success_response(self):
#         # Create an instance of a GET request.
#         request = self.factory.get('/v1/user/1/')

#         # Recall that middleware are not supported. You can simulate a
#         # logged-in user by setting request.user manually.
#         request.user = self.user

#         self.assertEqual(request.user.firstName, self.user.firstName)

#     #tearDown method is called after each test
#     def tearDown(self):
#         pass #nothing to tear down