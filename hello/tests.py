from django.test import TestCase
from django.urls import reverse

class HelloWorldTest(TestCase):
    def test_hello_world_view(self):
        """Test that the hello world view returns 'Welcome to Frobarn!'"""
        response = self.client.get(reverse('hello-world'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Welcome to Frobarn!")