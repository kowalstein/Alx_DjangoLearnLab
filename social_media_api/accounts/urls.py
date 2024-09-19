from django.urls import path
from .views import RegisterView, LoginView, ProfileView, FollowViewSet

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('follow/<int:used_id>/', FollowViewSet.as_view({'post': 'follow_user'}), name='follow_user'),
    path('unfollow/<int:user_id>/', FollowViewSet.as_view({'post': 'unfollow_user'}), name='unfollow_user'),
]
