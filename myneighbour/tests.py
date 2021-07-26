from django.test import TestCase
from .models import neighbourhood
from django.contrib.auth.models import User

# Create your tests here.
class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Langata = neighbourhood(neighbourhood='Langata')

    def test_instance(self):
        self.assertTrue(isinstance(self.Langata,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()