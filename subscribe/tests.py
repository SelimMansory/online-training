from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from course.models import Course
from subscribe.models import SubscribeUser
from users.models import User


class SubscribeTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(id=1, email='user@test.com', password='test', group='user', is_staff=True)
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            id=1,
            title='test',
            description='test',
            owner=self.user,
        )

        self.subscribe = SubscribeUser.objects.create(
            id=1,
            course=self.course,
            subscribe=True,
            user=self.user,
        )

    def test_list_subscribe(self):
        """ Тестирование вывода списка подписок"""
        response = self.client.get(
            reverse('subscribe:subscribe_list')
        )

        self.assertEquals(
            response.json(),
            [{'subscribe': True, 'course': 1, 'user': 1}]

        )

    def test_destroy_subscribe(self):
        """ Тестирование удаления подписки"""
        response = self.client.delete(
            reverse('subscribe:subscribe_destroy', kwargs={'pk': 1})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_create_subscribe(self):
        """ Тестирование создания подписки"""
        self.client.delete(reverse('subscribe:subscribe_destroy', kwargs={'pk': 1}))

        response = self.client.post(
            reverse('subscribe:subscribe_create'),
            data={
                'subscribe': True,
            }
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'subscribe': True, 'course': None, 'user': None}
        )