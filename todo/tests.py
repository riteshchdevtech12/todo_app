from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Todo
from .forms import TodoForm


class TodoListTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass'
        )
        self.client.login(username='testuser', password='testpass')
        Todo.objects.create(title='Test Todo', description='This is a test todo', author=self.user)

    def test_todo_list_view(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Todo')
        self.assertTemplateUsed(response, 'todo/todo_list.html')


class TodoDetailTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass'
        )
        self.client.login(username='testuser', password='testpass')
        self.todo = Todo.objects.create(title='Test Todo', description='This is a test todo', author=self.user)

    def test_todo_detail_view(self):
        response = self.client.get(reverse('todo_detail', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Todo')
        self.assertTemplateUsed(response, 'todo/todo_detail.html')


class TodoCreateTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass'
        )
        self.client.login(username='testuser', password='testpass')

    def test_todo_create_view(self):
        response = self.client.get(reverse('todo_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_form.html')
        form = response.context['form']
        self.assertIsInstance(form, TodoForm)
class TodoEditTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass'
        )
        self.client.login(username='testuser', password='testpass')
        self.todo = Todo.objects.create(title='Test Todo', description='This is a test todo', author=self.user)

    def test_todo_edit_view(self):
        response = self.client.get(reverse('todo_edit', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_form.html')
        form = response.context['form']
        self.assertIsInstance(form, TodoForm)

    def test_todo_edit_form_valid(self):
        data = {'title': 'New Title', 'description': 'This is a new description'}
        response = self.client.post(reverse('todo_edit', args=[self.todo.pk]), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('todo_detail', args=[self.todo.pk]))
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'New Title')
        self.assertEqual(self.todo.description, 'This is a new description')
