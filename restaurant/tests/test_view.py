from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from datetime import datetime
from faker import Faker

class TestViews(APITestCase):
    """
    Test all the restaurant api here
    """
    def setUp(self):
        client = APIClient()
        self.fake = Faker()
        self.login_url = '/api/v1/user/login/'
        self.signup_url = '/api/v1/user/signup/'
        self.winner_url = '/api/v1/restaurant/winner/'
        self.restaurant_url = '/api/v1/restaurant/restaurant/'
        self.user_data = {
            'email': self.fake.email(),
            'username': self.fake.email().split('@')[0],
            'password': self.fake.email(),
            'first_name': self.fake.name(),
        }
        client.post(self.signup_url, self.user_data, format='json' )
        res = client.post(self.login_url, self.user_data, format='json' )
        res = res.json()
        self.restaurant_data = {
            'name': self.fake.name(),
            'owner': res['id']
        }
        self.token = res['token']
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    
    def test_check_the_winner(self):
        """
        run before lunch time will get 400 and after lunch get 200.
        """
        response = self.client.get(self.winner_url, format='json')
        if datetime.today().hour > 13:
            self.assertEqual(response.status_code, 200)
        else:
            self.assertEqual(response.status_code, 400)

    def test_create_restaurant_with_no_token(self):
        """
        It will create a restaurant with 201 code
        """
        response = self.client.post(self.restaurant_url, self.restaurant_data, format='json')
        self.assertEqual(response.status_code, 401)
      
