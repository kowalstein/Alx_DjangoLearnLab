from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment, Like
from .serializers import PostSerializers, CommentSerializer
from notifications.models import Notification

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permissions_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['title']
    ordering_fields = ['created_at', 'title']
    ordering = ['created_at']

    def perform_created(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        post = self.get_object()
        if post.author != self.request.user:
            raise permissions.PermissionDenied("You do not have permission to edit this post.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise permissions.PermissionDenied("You do not have permission to delete this post.")
        instance.delete()

    def like_post(self, request, pk):
        post = self.get_object()
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
            return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)
    
    def unlike_post(self, response, pk):
        post = self.get_object()
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'status': 'unliked'}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({'status': 'not liked yet'}, status=status.HTTP_400_BAD_REQUEST)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        comment = self.get_object()
        if comment.author != self.request.user:
            raise permissions.PermissionDenied("You do not have permission to edit this comment.")
        serializer.save()
    
    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise permissions.PermissionDenied("You do not have permission to delete this comment.")
        instance.delete()

class FeedViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        followed_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializers = PostSerializers(posts, many=True)
        return Response(serializers.data)
    
