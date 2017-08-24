from django.test import TestCase
from pavelstanlley.models import Post
from django.core.urlresolvers import reverse
from django.test.client import Client
# Create your tests here.

class CategoryMethodTests(TestCase):
    def setUp(self):
        self.c= Client()
    def test_ensure_views_are_positive(self):
        response= self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    def test_about_access(self):
        response= self.c.get('/pavelstanlley/about/')
        self.assertEqual(response.status_code, 200)
    def test_contact_access(self):
        response= self.c.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
    def test_pavelstanlley_access(self):
        response= self.c.get('')
        self.assertEqual(response.status_code, 200)
    def test_restricted_create(self):
        response= self.c.get(reverse('restricted'))
        self.assertEqual(response.status_code,302)



