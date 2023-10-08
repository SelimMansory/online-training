from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.models import User


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(id=1, email='user@test.com', password='test', group='user', is_superuser=True)
        self.client.force_authenticate(user=self.user)

    def test_destroy_user(self):
        """ Тестирование удаление курса """
        response = self.client.delete(
            '/user/1/'
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_detail_user(self):
        """ Тестирование информация об пользователе """
        response = self.client.get(
            '/user/1/'
        )
        self.assertEquals(
            response.json(),
            {'id': 1, 'email': 'user@test.com', 'city': None, 'phone': None, 'first_name': '', 'last_name': '',
             'password': 'test', 'avatar': None, 'group': 'user'}
        )

    def test_list_user(self):
        """ Тест вывода списка пользователей """
        response = self.client.get(
            '/user/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            [{'id': 1, 'email': 'user@test.com', 'city': None, 'phone': None}]
        )

    def test_update_user(self):
        """ Тестирование обновление пользователя """
        response = self.client.put(
            '/user/1/',
            {'email': 'user@test.com',
             'password': 'new_test',
             'group': 'user',
             }
        )
        self.assertEquals(
            response.json(),
            [{'id': 1, 'email': 'user@test.com', 'city': None, 'phone': None, 'first_name': '', 'last_name': '',
              'password': 'test', 'avatar': None, 'group': 'user'}]

        )

    def test_create_user(self):
        """ Тестирование создание пользователя """
        self.client.delete('/user/1/')
        data = {'email': 'user@test.com',
             'password': 'test',
             'group': 'user',
             }
        response = self.client.post(
            '/user/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'email': 'user@test.com', 'city': None, 'phone': None}
        )