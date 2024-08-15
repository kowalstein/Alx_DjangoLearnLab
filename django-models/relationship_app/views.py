from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

from django.views.generic import DetailView
from .models import Library

def book_list_view(request):
    books = Book.objects.all()
    return HttpResponse(request, "relationship_app/list_books.html", {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

# Create your views here.
