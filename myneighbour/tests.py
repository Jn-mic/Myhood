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

    def save_method(self):
        self.Langata.save_neighbourhood()
        myhood=neighbourhood.objects.all()
        self.assertTrue(len(myhood)>0)
    
    def test_delete_method(self):
        self.Langata.delete_neighbourhood('Langata')
        myhood=neighbourhood.objects.all()
        self.assertTrue(len(myhood)==0)
        