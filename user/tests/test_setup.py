from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker

from user.models import CustomUser


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('user_signup')
        self.login_url = reverse('user_login')
        self.fake = Faker()

        self.user_data = {
            'email': self.fake.email(),
            'username': self.fake.email().split('@')[0],
            'password': self.fake.email(),
            'first_name': self.fake.name(),
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()