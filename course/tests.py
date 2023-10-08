from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from datetime import datetime
from course.models import Lesson, Course, Payments
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(id=1, email='user@test.com', password='test', group='user')
        self.client.force_authenticate(user=self.user)

        self.lesson = Lesson.objects.create(
            id=1,
            title='test',
            description='test',
            video_url='http://youtube.com',
            owner=self.user,
        )

    def test_destroy_lesson(self):
        """ Тестирование удаление урока """
        response = self.client.delete(
            reverse('course:lesson_delete', kwargs={'pk': 1})
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_detail_lesson(self):
        """ Тестирование информации об уроке """
        response = self.client.get(
            reverse('course:lesson_get', kwargs={'pk': 1})
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'title': 'test', 'preview': None, 'description': 'test', 'video_url': 'http://youtube.com',
             'course': None, 'owner': 1}
        )

    def test_list_lesson(self):
        """ Тестирование вывод списка уроков """
        response = self.client.get(
            reverse('course:lesson_list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 1, 'title': 'test', 'preview': None, 'description': 'test', 'video_url': 'http://youtube.com',
                 'course': None, 'owner': 1}]}

        )

    def test_update_lesson(self):
        """ Тестирование обновление урока """
        response = self.client.put(
            reverse('course:lesson_update', kwargs={'pk': 1}),
            {"title": 'new_test',
             "description": 'new_test',
             'video_url': 'http://youtube.com'}
        )
        self.assertEquals(
            response.json(),
            {'id': 1, 'title': 'new_test', 'preview': None, 'description': 'new_test',
             'video_url': 'http://youtube.com', 'course': None, 'owner': 1}

        )

    def test_create_lesson(self):
        """ Тестирование создание урока """
        self.client.delete(reverse('course:lesson_delete', kwargs={'pk': 1}))
        data = {
            "title": 'test',
            'description': 'test',
            "video_url": "http://youtube.com"
        }
        response = self.client.post(
            reverse('course:lesson_create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'title': 'test', 'preview': None, 'description': 'test', 'video_url': 'http://youtube.com',
             'course': None, 'owner': 1}
        )


class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(id=1, email='user@test.com', password='test', group='user')
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            id=1,
            title='test',
            description='test',
            owner=self.user,
        )

    def test_destroy_course(self):
        """ Тестирование удаление курса """
        response = self.client.delete(
            '/course/1/'
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_detail_course(self):
        """ Тестирование информация об курсе """
        response = self.client.get(
            '/course/1/'
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'count_lesson': 0, 'lesson': [], 'title': 'test', 'preview': None, 'subscribe': [],
             'description': 'test', 'owner': 1}
        )

    def test_list_course(self):
        """ Тестирование вывод списка курса """
        response = self.client.get(
            '/course/'
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.json(),
            [{'id': 1, 'count_lesson': 0, 'lesson': [], 'subscribe': [], 'title': 'test', 'preview': None,
              'description': 'test', 'owner': 1}]
        )

    def test_update_course(self):
        """ Тестирование обновление курса """
        response = self.client.put(
            '/course/1/',
            {"title": 'new_test',
             "description": 'new_test'
             }
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'count_lesson': 0, 'lesson': [], 'title': 'new_test', 'preview': None, 'subscribe': [],
             'description': 'new_test',
             'owner': 1}

        )

    def test_create_course(self):
        """ Тестирование создание курса """
        self.client.delete('/course/1/')
        data = {
            "title": 'test',
            'description': 'test',
            'owner': 1,
        }
        response = self.client.post(
            '/course/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'count_lesson': 0, 'lesson': [], 'title': 'test', 'preview': None, 'subscribe': [],
             'description': 'test', 'owner': 1}
        )


class PaymentsTestCase(APITestCase):
    date = datetime.now()

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(id=1, email='user@test.com', password='test', group='user', is_staff=True)
        self.client.force_authenticate(user=self.user)

        self.payment = Payments.objects.create(
            date_of_payment=self.date,
            payment_amount=100.0,
            payment_method='наличные',
            user=self.user,
        )

    def test_list_payments(self):
        """ Тестирование списка оплаты """
        response = self.client.get(
            reverse('course:payments_list')
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [{'user': {'id': 1, 'email': 'user@test.com',
                                                                               'city': None, 'phone': None,
                                                                               'first_name': '', 'last_name': '',
                                                                               'password': 'test', 'avatar': None,
                                                                               'group': 'user'},
                                                                      'date_of_payment': datetime.now().strftime(
                                                                          '%Y-%m-%d'),
                                                                      'payment_amount': 100.0,
                                                                      'payment_method': 'наличные'}]}

        )