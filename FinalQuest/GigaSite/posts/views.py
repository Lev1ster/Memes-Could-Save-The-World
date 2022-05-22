from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from . import serializers
from .models import Post, UserSubscribe, PostRead
from .paginator import UserPostsResultsPagination

# Create your views here.

class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(id_user=self.request.user)