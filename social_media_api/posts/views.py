from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import PostSerializers, CommentSerializer

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
