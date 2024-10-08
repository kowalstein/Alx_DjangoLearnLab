from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from .models import Library

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required


def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Assuming the related_name for books in Library model is 'books'
        return context

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class LoginView(LoginView):
    template_name = 'relationship_app/login.html'
    success_url = reverse_lazy('home')
    redirect_authenticated_user = True

class LogoutView(LogoutView):
    next_page = reverse_lazy('home')

@login_required
def home(request):
    return render(request, 'home.html') # NEEDS WORK



@user_passes_test(lambda u: u.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda u: u.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda u: u.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'add_book.html')
    
@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        pass
    else:
        return render(request, 'edit_book.html', {'book': book})
    
@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    else:
        return render(request, 'confirm_delete.html', {'book': book})
# Create your views here.
