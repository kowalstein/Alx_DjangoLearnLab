from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser')
        self.client.login(username='testuser', password='testpassword')
        self.create_url = reverse('book-list')
        self.book = Book.objects.create(title='Test Book', author='Author', publication_year=2022)
    
    def test_create_book(self):
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2023}
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(pk=response.data['id']).title, 'New Book')

    def test_read_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book.id])
        data = {'title': 'Updated Book'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=self.book.id).title, 'Updated Book')

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        url = f"{self.create_url}?title=Test Book"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_search_books(self):
        url = f"{self.create_url}?search=Test"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_order_books(self):
        url = f"{self.create_url}?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['publication_year'], 2023)

    def test_unauthorized_access(self):
        self.client.logout()
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
