from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from models.services.models import Event

import json

class TestEvent(TestCase):

