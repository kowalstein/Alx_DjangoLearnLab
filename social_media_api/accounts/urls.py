from django.urls import path
from .views import RegisterView, LoginView, ProfileView, FollowViewSet, UnfollowViewSet

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('follow/<int:used_id>/', FollowViewSet.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowViewSet.as_view(), name='unfollow_user'),
]
