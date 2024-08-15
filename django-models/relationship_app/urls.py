from django.urls import path
from . import views
from .views import LoginView, LogoutView
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name="book-list"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
    path('register/', views.register,  name='register'),
    path('login/', LoginView.as_view(template_name='relationshi_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationshi_app/logout.html'), name='logout'),
    path('logout/done/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout_done'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]