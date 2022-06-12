import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from mainapp.views import UserModelViewSet
from todoapp.models import TODO


class TestUserViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {
            'first_name': 'Иванов',
            'last_name': 'Петр',
            'email': 'nomail@mail.ru'},
                               format='json')
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {
            'first_name': 'Пушкин',
            'last_name': 1799,
            'email': 'nomail@mail.ru'},
                               format='json')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        force_authenticate(request, admin)
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        user = User.objects.create(first_name='Иванов', last_name='Петр', email='nomail@mail.ru')
        client = APIClient()
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        user = User.objects.create(first_name='Иванов', last_name='Петр', email='nomail@mail.ru')
        client = APIClient()
        response = client.put(f'/api/users/{user.id}/',
                              {'first_name': 'Иванов', 'last_name': 'Петр', 'email': 'nomail@mail.ru'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        user = User.objects.create(first_name='Иванов', last_name='Петр', email='nomail@mail.ru')
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        client.login(username='admin', password='admin123456')
        response = client.put(f'/api/users/{user.id}/',
                              {'first_name': 'Иванов', 'last_name': 'Петр', 'email': 'nomail@mail.ru'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(user.first_name, 'Иванов')
        self.assertEqual(user.last_name, 'Петр')
        self.assertEqual(user.email, 'nomail@mail.ru')
        client.logout()


class TestMath(APISimpleTestCase):
    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)


class TestTODOViewSet(APITestCase):
    def test_get_lists(self):
        response = self.client.get('api/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_todo_admin(self):
        todo = mixer.blend(TODO)

        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = client.put(f'/api/todos/{todo.id}/',
                              {'todo_project': 'Ежедневник', 'text': 'Напоминание'})
        todo = TODO.objects.get(pk=todo.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(todo.todo_project, 'Ежедневник')
        self.assertEqual(todo.text, 'Напоминание')
