from django.shortcuts import render
from .forms import ExampleForm
# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    articles = Book.objects.all()
    return render(request, 'book_list.html', {'books': Book})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        # Handle form submission to create a new article
        pass
    return render(request, 'article_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Handle form submission to edit the article
        pass
    return render(request, 'book_form.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})

def book_list(request):
    form = ExampleForm(request.GET)
    if form.is_valid():
        search_query = form.cleaned_data.get('search', '')
        books = Book.objects.filter(title__icontains=search_query)
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})
