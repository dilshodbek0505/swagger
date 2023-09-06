from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Comment, Post
from .serializer import PostSerializer, CommentSerializer
# Create your views here.

class PostApi(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class CommentApi(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.select_related('post').all()

class PostEditApi(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class CommentEditApi(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.select_related('post').all()