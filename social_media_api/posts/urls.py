from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:pk>/like/', PostViewSet.as_view({'post': 'like_post'}), name='like_post'),
    path('post/<int:pk>/unlike/', PostViewSet.as_view({'post': 'unlike_post'}), name='unlike_post'),
]

urlpatterns += [
    path('feed/', FeedViewSet.as_view({'get': 'list'}), name='feed'),
]