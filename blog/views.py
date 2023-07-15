from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    CommentSerializer,
    BlogSerializer,
)
from .models import (
    Blog,
    Comment,
)
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrStaffOrReadOnly


class BlogViewset(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.filter(status='p')
    permission_classes = [
        IsAuthenticatedOrReadOnly, 
        IsOwnerOrStaffOrReadOnly
        ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentView(CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(commentor=self.request.user)
