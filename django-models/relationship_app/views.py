from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

from django.views.generic import DetailView
from .models import Library

def book_list_view(request):
    books = Book.objects.all()
    response_text = "<h1>Books List<h1>"
    for book in books:
        response_text += f"<p>Title: {book.title}, Author: {book.author}</p>"
    return HttpResponse(response_text)

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

# Create your views here.
