from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet


router =  DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('api/', include(router.urls)),
]
