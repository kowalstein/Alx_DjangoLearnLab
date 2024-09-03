from django.urls import path
from .views import BookListView, BookDetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create', CreateView.as_view(), name='create'),
    path('books/update', UpdateView.as_view(), name='update'),
    path('books/delete', DeleteView.as_view(), name='delete'),
]
