from django.test import TestCase
from django.test import Client

class test_app(TestCase):

    def __init__(self):
        self.client = Client()

    def goto_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        return response

    def get_agents(self):
        response =  self.client.get('/agents/')
        self.assertEqual(response.status_code, 200)
        return response


if __name__ == "__main__":
    obj = test_app()
    obj.get_agents()
