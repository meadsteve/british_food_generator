from django.test import TestCase, Client

class SmokeTests(TestCase):
    client = Client()

    def test_the_minimum_possible_works(self):
        response = self.client.get('/')
        assert response.status_code == 200